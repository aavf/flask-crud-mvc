# -*- coding: utf-8 -*-
import os
# third-party imports
from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# local imports
from config import app_config


# variables initialization
db = SQLAlchemy() # ORM substitutes raw sql
login_manager = LoginManager()


def create_app(config_name):
    # production or developmento config
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    db.init_app(app)

    migrate = Migrate(app, db) # to syncronize models files to database

    login_manager.init_app(app)
    login_manager.login_message = "Página para utilizadores registados"
    login_manager.login_view = "auth.login"

    @app.route('/')
    def index():
        return redirect(url_for('person.list_persons'))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(403)
    def page_not_found(e):
        return render_template('403.html'), 403

    # register modules / components
    from .persons import person as person_blueprint
    app.register_blueprint(person_blueprint)

    from .users import user as user_blueprint
    app.register_blueprint(user_blueprint)

    # authentication module
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
