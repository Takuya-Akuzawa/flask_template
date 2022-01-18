import os
from random import choice
import string


class Development(object):
    DEBUG = True
    SECRET_KEY = "".join([choice(string.ascii_letters + string.digits + '_' + '-' + '!' + '#' + '&') for i in range(64)])
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myflask.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

def init_config(app):
    """
    環境変数FLASK_APP_ENVの設定値(production/development)を読み取り、
    環境に応じたクラスからapp.configを設定する。

    Args:
        app
    Return:
        None
    """
    flask_app_env = os.getenv('FLASK_APP_ENV', 'production')
    config_type = {
        "development":  "flask_package.config.Development",
        "production": "flask_package.config.Production"
        # appパッケージ > configモジュール > Developmentコンポーネント(クラス)を読み込む
    }
    app.config.from_object(config_type.get(flask_app_env))
    return