import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_package.config import FlaskConfig

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login' # type: ignore

def page_not_found(e):
    return render_template('error_page.html',
                            code=e.code,
                            title=e.name,
                            messages={
                                'lead': 'リクエストされたページが見つかりませんでした。',
                                'description': e.description,}
                            ), 404


def create_app():
    FlaskConfig.logging_config()

    app = Flask(__name__, instance_relative_config=True)
    app.logger.info(f'Created Flask app: {app.name}')
    
    # Set configuration for db access info, ...etc
    FlaskConfig.env_config(app)
    app.logger.info('Configured Environment Variables')
    
    initialize_extensions(app)
    app.logger.info('Initialized DB')
    
    register_blueprints(app)
    app.logger.info('Registered Blueprints')
    
    app.register_error_handler(404, page_not_found) #type: ignore

    return app


def initialize_extensions(app):
    # Since the application instance is now created,
    # pass it to each Flask extension instance
    # to bind it to the Flask application instance (app)
    db.init_app(app)
    Migrate(app, db)
    # Flask-Login configuration
    login.init_app(app)
    from flask_package.models import User
    
    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from flask_package.view_sample.routes import views_blueprint
    from flask_package.auth import auth_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(views_blueprint)


