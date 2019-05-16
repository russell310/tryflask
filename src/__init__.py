# third-party imports
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from .settings import app_config, BASE_DIR

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile(os.path.join(BASE_DIR, 'src', 'settings.py'))
    app.template_folder = os.path.join(BASE_DIR, 'templates')
    app.static_folder = os.path.join(BASE_DIR, 'static')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    # from app import models

    from apps.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from apps.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from apps.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
