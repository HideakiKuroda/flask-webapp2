import requests

def user_info(auth, app_config=None):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Accept': 'application/json'
    }

    endpoint = "https://graph.microsoft.com/v1.0/me"
    
    response = requests.get(endpoint, headers=headers)
    user_info = response.json()

    return user_info    


# __init__.py
import identity.web
from flask import Flask, session
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix
from . import app_config
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

# logins.views.py
from flask import render_template, request, url_for, redirect
from flask import Blueprint
from ntb_marine import app_config, auth, __version__, app
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
