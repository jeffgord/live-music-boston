from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/location/<id>")
def location(id):
    return render_template("location.html", location_name=id)
