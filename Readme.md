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
flask_package/
├── __init__.py
├── config.py
├── models
│   ├── __init__.py
│   └── user.py
├── templates
│   └── index.html
└── views.py
```

<br>

## 環境変数について
```
FLASK_APP_ENV=development
FLASK_APP=flask_package:app
```
flask_packageのappコンポーネント(Flaskインスタンス)を実行するという意味。

app/__init__.pyでFlask()が生成されている。

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
gunicorn flask_package:app -c gunicorn_settings.py
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





