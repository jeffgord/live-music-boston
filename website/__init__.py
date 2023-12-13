from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "change this for production"  # todo
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views.views import views
    from .views.admin import admin
    from .views.maintenance import maintenance

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")
    app.register_blueprint(maintenance, url_prefix="/")

    from . import models

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.login_message = "Admin access only!"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_admin(id):
        return models.Admin.query.get(int(id))

    return app
