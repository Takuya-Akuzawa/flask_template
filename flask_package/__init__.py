import os

from flask import Flask

from flask_package.models import init_db
from flask_package.models.user import User
from flask_package.views import views
from flask_package.config import init_config

app = Flask(__name__, instance_relative_config=True)

# configの読み込み Sqlite接続情報
init_config(app)

# DBの設定
init_db(app)

# モジュール分割したBlueprintの登録
app.register_blueprint(views)