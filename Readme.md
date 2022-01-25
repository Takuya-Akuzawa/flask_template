# 本リポジトリについて
- Flaskアプリケーションの雛形ファイルをflask_packageとして保存・再利用する
- Flaskアプリ構築用のDocker開発環境をセットアップする

<br>

## Docker環境構築手順
---
Dockerfileがあるディレクトリで実行
1. コンテナイメージのビルド
```
docker image build -t practice/my_flask:latest .
```
2. イメージからコンテナを起動。
```
docker container run -it --rm -p 5050:5050 -v ${PWD}:/usr/src/app --name myflask practice/my_flask:latest
```
- localhost:5050をポートフォワーディング
- カレントディレクトリに/usr/src/appをVolumeマウント
- exit時にコンテナ削除

<br>

## パッケージ構造
```
flask_package
├── __init__.py
├── config.py
├── models.py
├── log
│   └── flask_app.log
├── static
│   └── main.css
├── templates
│   ├── base.html
│   ├── error_page.html
│   └── flash_message.html
├── auth
│   ├── __init__.py
│   ├── forms.py
│   ├── routes.py
│   └── templates
│       ├── login.html
│       ├── profile.html
│       └── register.html
└── view_sample
    ├── __init__.py
    ├── routes.py
    └── templates
        └── index.html
```

<br>

## 環境変数について

```
FLASK_APP_ENV=development
FLASK_APP="flask_package:create_app()"
```
flask_packageのcreate_app()からFlaskインスタンスを生成し起動する。

※ `flask_package/__init__.py`でcreate_app()を定義。

<br>

## Flask-MigrateでDBテーブル作成
- config.pyでDB接続先を設定
- flask_packageの存在するディレクトリから実行
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

<br>

## Flaskアプリ実行方法
flask_packageの存在するディレクトリから実行する。
- flask run で実行
```
flask run -h 0.0.0.0 -p 5050
```
※ Dockerで設定したポート番号で起動する。

<br>

- gunicornで実行
```
gunicorn -c gunicorn_settings.py
```
 
 <br>

- uWSGIで実行
```
uwsgi uwsgi.ini
```
<br>

## ローカル環境設定
VSCodeでの静的解析用にPython仮想環境を作成し、各種ライブラリをインストールする。
- pyenvでバージョンを変更
```
pyenv global 3.7.10
python -V
```
- venv操作
```
# venv作成、起動
python -m venv venv
source venv/bin/activate

# venv終了
deactivate

# venv削除
rm -r venv
```
- venv環境で各種ライブラリをインストール
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

## pytest実行
flask_packageの存在するディレクトリから実行する
```
python -m pytest tests --cov --cov-report=term-missing -v

# options
--cov-report=term-missing
--flakes
--setup-show
-v
```




