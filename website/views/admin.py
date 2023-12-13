from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from .. import db
from ..models import Admin


admin = Blueprint("admin", __name__)


@admin.route("/admin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            return redirect(url_for("maintenance.page"))
        else:
            flash("Hey! Those credentials are no good.")

    return render_template("admin-login.html")


@admin.before_request
def automatic_logout():
    if (
        request.endpoint
        and "admin" not in request.endpoint
        and current_user.is_authenticated
    ):
        logout_user()
