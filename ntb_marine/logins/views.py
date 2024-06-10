from flask import render_template, request, url_for, redirect, flash, abort
from flask import Blueprint
from ntb_marine import app_config, auth, __version__, app
from ntb_marine import ms_file_control 
import requests

logins = Blueprint('logins', __name__)

@logins.route("/login")
def login():
    return render_template("login.html", version=__version__, **auth.log_in(
        scopes=app_config.SCOPE,
        redirect_uri=url_for("logins.auth_response", _external=True),
        prompt="select_account",
    ))

@logins.route(app_config.REDIRECT_PATH)
def auth_response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("auth_error.html", result=result)
    return redirect(url_for("logins.index"))

@logins.route("/logout")
def logout():
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
    return render_template('display.html', result=api_result,user_info=user_info)

