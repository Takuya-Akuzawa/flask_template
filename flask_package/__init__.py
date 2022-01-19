import os

from flask import Flask

from flask_package.config import FlaskConfig
from flask_package.models import init_db
# modelクラスを以下にimport
from flask_package.models.user import User
# viewのBlueprintを以下にimport
from flask_package.views import views


FlaskConfig.logging_config()

app = Flask(__name__, instance_relative_config=True)
app.logger.info(f'Flaskアプリケーション[{app.name}]を起動')

# configの読み込み Sqlite接続情報
FlaskConfig.env_config(app)
app.logger.info('Flaskアプリケーションへの環境変数の設定完了')

# DBの設定
init_db(app)
app.logger.info('DBの初期化完了')

# モジュール分割したBlueprintの登録
app.register_blueprint(views)
app.logger.info('Blueprintの登録完了')