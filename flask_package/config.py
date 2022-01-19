from logging.config import dictConfig
import os
from random import choice
import string
import logging

from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    """request情報をformatterに埋め込むためのサブクラス"""

    def format(self, record):
        if has_request_context():
            record.remote_addr = request.remote_addr
            record.method = request.method
            record.url = request.url
        else:
            record.remote_addr = None
            record.method = None
            record.url = None

        return super().format(record)


class FlaskConfig(object):
    """Flaskアプリケーションの環境変数、logging設定を行うクラス"""

    # dictConfigで読み込む設定を辞書型で保持
    logging_property = dict({
        'version': 1,
        # フォーマットの設定
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
            },
            'request': {
                '()': RequestFormatter,
                'format': '[%(asctime)s][%(levelname)s] %(module)s %(remote_addr)s -> %(url)s : %(message)s'
            }
        },
        # ハンドラの設定
        'handlers': {
            'wsgi': {  # 標準出力用ハンドラ
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'request',
            },
            'customFileHandler': {  # logファイル出力用ハンドラ
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'request',
                'filename': 'flask_package/log/flask_app.log',
                'maxBytes': 3 * 1024 * 1024,
                'backupCount': 3,
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi', 'customFileHandler'],
        }
    })

    @classmethod
    def logging_config(cls):
        """logging設定を実施する。"""
        dictConfig(cls.logging_property)
        return

    @classmethod
    def env_config(cls, app):
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
            # flask_packageパッケージ > configモジュール > Developmentコンポーネント(クラス)を読み込む
        }
        app.config.from_object(config_type.get(flask_app_env))
        return


class Development(object):
    """development用の環境変数設定クラス"""
    DEBUG = True
    SECRET_KEY = "".join([choice(string.ascii_letters + string.digits +
                         '_' + '-' + '!' + '#' + '&') for i in range(64)])
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite_flask.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

