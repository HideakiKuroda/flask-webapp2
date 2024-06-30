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

# アプリケーションのルートディレクトリを取得
basedir = os.path.abspath(os.path.dirname(__file__))
# データベースの相対パスを設定
database_path = os.path.join(basedir, 'instance', 'ntb.db')
sqlPath = f"sqlite:///{database_path}"
print(f'SQLite path1: {sqlPath}')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #データベースの変更履歴は不要
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
sqlPath = os.getenv("SQLALCHEMY_DATABASE_URI")

print(f'SQLite path2: {sqlPath}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #データベースの変更履歴は不要
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
from ntb_marine.document.views import document

app.register_blueprint(logins)
app.register_blueprint(file_control)
app.register_blueprint(document)




# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000)
# az webapp config set --resource-group ntbResourceGroup --name ntb-marine --startup-file startup.sh    
# deploy
# az webapp up --resource-group ntbResourceGroup --name ntb-marine

# az webapp up --runtime PYTHON:3.11 --sku B1 --logs
# https://ntb-marine.azurewebsites.net
        
