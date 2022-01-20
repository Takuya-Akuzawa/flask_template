import traceback

from flask import Blueprint, render_template, current_app
from flask_package.models import db

views = Blueprint('views_module', __name__, template_folder='templates')


@views.route('/')
def index():
    logger = current_app.logger
    logger.info('index.html表示')
    return render_template('index.html')