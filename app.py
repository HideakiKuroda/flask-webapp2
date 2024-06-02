import identity.web
from flask import Flask, redirect, render_template, request, session, url_for, flash, send_file, abort
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix
from io import BytesIO
import requests
import app_config
import ms_file_control
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

__version__ = "0.8.0"

app = Flask(__name__)
# app.secret_key = app_config.SECRET_KEY
app.config.from_object(app_config)
assert app.config["REDIRECT_PATH"] != "/", "REDIRECT_PATH must not be /"
app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True,
    SESSION_TYPE="filesystem"
)
Session(app)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

app.jinja_env.globals.update(Auth=identity.web.Auth)
auth = identity.web.Auth(
    session=session,
    authority=app.config["AUTHORITY"],
    client_id=app.config["CLIENT_ID"],
    client_credential=app.config["CLIENT_SECRET"],
)
tenant_id = app.config["TENANT_ID"]
client_id = app.config["CLIENT_ID"]
client_secret = app.config["CLIENT_SECRET"]

@app.route("/login")
def login():
    return render_template("login.html", version=__version__, **auth.log_in(
        scopes=app_config.SCOPE,
        redirect_uri=url_for("auth_response", _external=True),
        prompt="select_account",
    ))

# @app.route(app_config.REDIRECT_PATH)
# def auth_response():
#     result = auth.complete_log_in(request.args)
#     if "error" in result:
#         return render_template("auth_error.html", result=result)
#     return redirect(url_for("index"))
@app.route(app_config.REDIRECT_PATH)
def auth_response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("auth_error.html", result=result)

    # ここでアクセストークンを取得する
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default"
    }
    response = requests.post(token_url, data=data)
    access_token = response.json()["access_token"]

    # アクセストークンを使用して Microsoft Graph API を呼び出す
    graph_url = "https://graph.microsoft.com/v1.0/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(graph_url, headers=headers)
    user_info = response.json()
    # user_info = {k: v for k, v in user_info.items() if v is not None and v != 'undefined'}
    print(type(user_info['name']))
    # ユーザー情報をセッションに保存する
    session["user_info"] = user_info

    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    return redirect(auth.log_out(url_for("index", _external=True)))

@app.route("/")
def index():
    if not (app.config["CLIENT_ID"] and app.config["CLIENT_SECRET"]):
        return render_template('config_error.html')
    if not auth.get_user():
        return redirect(url_for("login"))
    return render_template('index.html', user=auth.get_user(), version=__version__)

@app.route("/call_downstream_api")
def call_downstream_api():
    token = auth.get_token_for_user(app_config.SCOPE)
    if "error" in token:
        return redirect(url_for("login"))
    
     # セッションからユーザー情報を取得する
    user_info = session.get("user_info")

    api_result = requests.get(
        app_config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
        timeout=30,
    ).json()
    return render_template('display.html', result=api_result,user_info=user_info)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません。")
            return redirect(request.url)
        
        file = request.files["file"]
        
        if file.filename == "":
            flash("ファイルが選択されていません。")
            return redirect(request.url)

        if file:
            result = ms_file_control.upload_file_to_sharepoint(file, auth, app_config)
            if result:
                flash("ファイルが正常にアップロードされました。")
            else:
                flash("ファイルのアップロードに失敗しました。")
            return redirect(url_for("index"))
    return render_template("upload.html", username=auth.get_user()["name"])

@app.route("/list_files", methods=["GET"])
@app.route("/list_files/<folder_id>", methods=["GET"])
def list_files(folder_id=None):
    files, folders, file_ids, folder_ids, status = ms_file_control.list_files(auth, folder_id, app_config)
    if status!= 200:
        return  status
    return render_template("file_list.html", files=files, folders=folders)

@app.route("/download/<file_id>/<file_name>", methods=["GET"])
def download_file(file_id, file_name):
    file_content, status = ms_file_control.download_file(file_id, auth, app_config)
    if status!= 200:
        return  status
    return send_file(file_content, as_attachment=True, download_name=file_name)

@app.route("/create_folder", methods=["POST","GET"])
def create_folder():
    folder_name = request.form.get("folder_name")
    if not folder_name:
        return render_template('create_folder.html')
    folder_id, status = ms_file_control.create_folder(folder_name, auth, app_config)
    if status not in [200, 201]:
        flash("error: Could not create folder")
        return redirect(url_for("index"))
    
    flash(f"フォルダが正常に作成されました。フォルダID: {folder_id}")
    return redirect(url_for("upload_to_folder_page", folder_id=folder_id))

@app.route("/upload_to_folder_page/<folder_id>", methods=["GET", "POST"])
def upload_to_folder_page(folder_id):
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません。")
            return redirect(request.url)
        
        file = request.files["file"]
        
        if file.filename == "":
            flash("ファイルが選択されていません。")
            return redirect(request.url)

        if file:
            result = ms_file_control.upload_file_to_specific_folder(file, folder_id, auth, app_config)
            if result:
                flash("ファイルが正常にアップロードされました。")
            else:
                flash("ファイルのアップロードに失敗しました。")
            return redirect(url_for("index"))
    return render_template("upload_to_folder.html", folder_id=folder_id)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000)
# az webapp config set --resource-group ntbResourceGroup --name ntb-marine --startup-file startup.sh    
# deploy
# az webapp up --resource-group ntbResourceGroup --name ntb-marine

# az webapp up --runtime PYTHON:3.11 --sku B1 --logs
# https://ntb-marine.azurewebsites.net
        
