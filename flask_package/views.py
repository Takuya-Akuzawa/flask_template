import traceback

from flask import Blueprint, render_template, current_app
from flask_package.models import db

views = Blueprint('views_module', __name__, template_folder='templates')

@views.route('/')
def index():
    logger = current_app.logger
    logger.info('index.html表示')
    return render_template('index.html')


@views.errorhandler(404)
def page_not_found(error):
    return render_template('error_page.html',
                            code=error.code,
                            title=error.name,
                            messages={
                                'lead': 'リクエストされたページが見つかりませんでした。',
                                'description': error.description,}
                            ), 404


@views.errorhandler(Exception)
def other_error(error):
    return render_template('error_page.html',
                            code='???',
                            title='Unexpected Error',
                            messages={
                                'lead': 'システムエラーが発生しました。',
                                'description': traceback.format_exc()}
                            ), 503