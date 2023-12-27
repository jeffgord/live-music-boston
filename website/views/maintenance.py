from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    session,
    jsonify,
)
from flask_login import login_required
from sqlalchemy import func
from .. import db
from ..models import Location, Venue


maintenance = Blueprint("maintenance", __name__)


@maintenance.route("/maintenance")
@login_required
def page():
    return render_template("maintenance.html")


@maintenance.route("/maintenance/locations")
def locations():
    locations = list(Location.query.all())
    locations.sort(key=lambda location: location.ordinal)

    data = []
    for location in locations:
        data.append({"id": location.id, "name": location.name})

    return jsonify({"data": data})
