from flask import Blueprint, render_template
from ..utils import venue_service

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/location/<location>")
def location(location):
    venues = venue_service.get_venues(location)
    location_name = get_proper_location_name(location)
    return render_template("location.html", location_name=location_name, venues=venues)


def get_proper_location_name(location):
    match location:
        case "allbright":
            return "Allston/Brighton"
        case "camberville":
            return "Cambridge/Somerville"
        case "downtown":
            return "Downtown"
        case "elsewhere":
            return "Elsewhere"
        case _:
            raise NotImplementedError
