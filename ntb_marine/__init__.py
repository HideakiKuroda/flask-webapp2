import identity.web
from flask import Flask, redirect, render_template, request, session, url_for, flash, send_file, abort
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix
from io import BytesIO
import requests
from . import app_config
from . import ms_file_control
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


# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     if request.method == "POST":
#         if "file" not in request.files:
#             flash("ファイルが選択されていません。")
#             return redirect(request.url)
        
#         file = request.files["file"]
        
#         if file.filename == "":
#             flash("ファイルが選択されていません。")
#             return redirect(request.url)

#         if file:
#             result = ms_file_control.upload_file_to_sharepoint(file, auth, app_config)
#             if result:
#                 flash("ファイルが正常にアップロードされました。")
#             else:
#                 flash("ファイルのアップロードに失敗しました。")
#             return redirect(url_for("logins.index"))
#     return render_template("upload.html", username=auth.get_user()["name"])

# @app.route("/list_files", methods=["GET"])
# @app.route("/list_files/<folder_id>", methods=["GET"])
# def list_files(folder_id=None):
#     files, folders, file_ids, folder_ids, status = ms_file_control.list_files(auth, folder_id, app_config)
#     if status!= 200:
#         return  status
#     return render_template("file_list.html", files=files, folders=folders)

# @app.route("/download/<file_id>/<file_name>", methods=["GET"])
# def download_file(file_id, file_name):
#     file_content, status = ms_file_control.download_file(file_id, auth, app_config)
#     if status!= 200:
#         return  status
#     return send_file(file_content, as_attachment=True, download_name=file_name)

# @app.route("/create_folder", methods=["POST","GET"])
# def create_folder():
#     folder_name = request.form.get("folder_name")
#     if not folder_name:
#         return render_template('create_folder.html')
#     folder_id, status = ms_file_control.create_folder(folder_name, auth, app_config)
#     if status not in [200, 201]:
#         flash("error: Could not create folder")
#         return redirect(url_for("logins.index"))
    
#     flash(f"フォルダが正常に作成されました。フォルダID: {folder_id}")
#     return redirect(url_for("upload_to_folder_page", folder_id=folder_id))

# @app.route("/upload_to_folder_page/<folder_id>", methods=["GET", "POST"])
# def upload_to_folder_page(folder_id):
#     if request.method == "POST":
#         if "file" not in request.files:
#             flash("ファイルが選択されていません。")
#             return redirect(request.url)
        
#         file = request.files["file"]
        
#         if file.filename == "":
#             flash("ファイルが選択されていません。")
#             return redirect(request.url)

#         if file:
#             result = ms_file_control.upload_file_to_specific_folder(file, folder_id, auth, app_config)
#             if result:
#                 flash("ファイルが正常にアップロードされました。")
#             else:
#                 flash("ファイルのアップロードに失敗しました。")
#             return redirect(url_for("logins.index"))
#     return render_template("upload_to_folder.html", folder_id=folder_id)

from ntb_marine.logins.views import logins
from ntb_marine.file_control.views import file_control

app.register_blueprint(logins)
app.register_blueprint(file_control)



# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000)
# az webapp config set --resource-group ntbResourceGroup --name ntb-marine --startup-file startup.sh    
# deploy
# az webapp up --resource-group ntbResourceGroup --name ntb-marine

# az webapp up --runtime PYTHON:3.11 --sku B1 --logs
# https://ntb-marine.azurewebsites.net
        
