from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from . import db
from .models import *


admin = Blueprint("admin", __name__)


@admin.route("/admin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            return redirect(url_for("admin.maintenance"))
        else:
            flash("Hey! Those credentials are no good.")

    return render_template("admin-login.html")


@admin.route("/maintenance")
@login_required
def maintenance():
    locations = Location.query.all()
    venues = Venue.query.all()
    return render_template("maintenance.html", locations=locations, venues=venues)


@admin.route("/maintenance/add-location", methods=["POST"])
@login_required
def add_location():
    name = request.form["name"]

    if Location.query.filter_by(name=name).first():
        flash("A location already exists with that name!")
    else:
        new_location = Location(name=name)
        db.session.add(new_location)
        db.session.commit()

    return redirect(url_for("admin.maintenance"))


@admin.before_request
def automatic_logout():
    if (
        request.endpoint
        and "admin" not in request.endpoint
        and current_user.is_authenticated
    ):
        logout_user()
