import os

from flask import Flask

from flask_package.config import init_config
from flask_package.models import init_db
# modelクラスを以下にimport
from flask_package.models.user import User
# viewのBlueprintを以下にimport
from flask_package.views import views


app = Flask(__name__, instance_relative_config=True)

# configの読み込み Sqlite接続情報
init_config(app)

# DBの設定
init_db(app)

# モジュール分割したBlueprintの登録
app.register_blueprint(views)