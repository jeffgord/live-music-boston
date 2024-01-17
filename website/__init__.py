from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "change this for production"  # todo

    from .views.views import views

    app.register_blueprint(views, url_prefix="/")

    return app
