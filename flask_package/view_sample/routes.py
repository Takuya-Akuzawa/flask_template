#################
#### imports ####
#################
from flask import render_template, current_app

from . import views_blueprint
from flask_package import db

@views_blueprint.route('/')
def index():
    logger = current_app.logger
    logger.info('return index.html')
    return render_template('index.html')