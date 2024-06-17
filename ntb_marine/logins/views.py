from flask import render_template, request, url_for, redirect, flash, abort
from flask import Blueprint
from ntb_marine import app_config, auth, __version__, app, db
from ntb_marine import ms_file_control
from ntb_marine.models import User
import requests
from flask_login import login_user, LoginManager,login_user, logout_user, login_required, current_user 

logins = Blueprint('logins', __name__)

login_manager = LoginManager() #インスタンス化
login_manager.init_app(app)  #appとログイン機能を紐づけ

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@logins.route("/login")
def login():
    return render_template("users/login.html", version=__version__, **auth.log_in(
        scopes=app_config.SCOPE,
        redirect_uri=url_for("logins.auth_response", _external=True),
        prompt="select_account",
    ))

@logins.route(app_config.REDIRECT_PATH)
def auth_response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("auth_error.html", result=result)
    
    user_info = ms_file_control.user_info(auth, app_config)

    # ログインしたユーザーを、User モデルのインスタンスにマッピングします。
    user = User.query.filter_by(ms_email=user_info["mail"]).first()
    # ユーザーが登録されていない場合は、新しいユーザーを作成します。
    if not user:
        user = User(email="", name=user_info["displayName"], ms_email=user_info["mail"], ms_id=user_info["id"])
        db.session.add(user)
        db.session.commit()
    # ユーザーが既に登録されている場合で、idが空白の場合はそのユーザーidを入力します。
    if user.ms_id is None or user.ms_id == "":
        # ユーザーは登録されているが、ID が登録されていない場合は、ID を登録します。
        user.ms_id = user_info["id"]
        db.session.commit() 

    # ユーザーをログインします。
    login_user(user)
    # print(f"ユーザーID: {user.id}")

    return redirect(url_for("logins.index"))

@logins.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(auth.log_out(url_for("logins.index", _external=True)))

@logins.route("/")
def index():
    if not (app.config["CLIENT_ID"] and app.config["CLIENT_SECRET"]):
        return render_template('config_error.html')
    if not auth.get_user():
        return redirect(url_for("logins.login"))
    user_info = ms_file_control.user_info(auth, app_config)
    username = user_info["displayName"]
    mail = user_info["mail"]
    return render_template('index.html', user=auth.get_user(), username=username,mail=mail, version=__version__)

@logins.route("/call_downstream_api")
def call_downstream_api():
    token = auth.get_token_for_user(app_config.SCOPE)
    if "error" in token:
        return redirect(url_for("logins.login"))
    
     # セッションからユーザー情報を取得する
    user_info = ms_file_control.user_info(auth, app_config)

    api_result = requests.get(
        app_config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
        timeout=30,
    ).json()
    return render_template('file_control/display.html', result=api_result,user_info=user_info)

