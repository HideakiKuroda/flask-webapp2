import identity.web
from flask import Flask, session, current_app
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix
from . import app_config
from dotenv import load_dotenv
import logging
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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

# basedir = os.path.abspath(os.path.dirname(__file__))  
# # data.sqlite という名前のデータベースを作成します。
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #データベースの変更履歴は不要
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#"Migrate" の設定
Migrate(app, db)
# データベースの作成
#リレーションシップを"SQLite3"で有効化するためのコード（SQLAlchemy 1.4 Documentation「Foreign Key Support」より）
from sqlalchemy.engine import Engine
from sqlalchemy import event
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


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
        
