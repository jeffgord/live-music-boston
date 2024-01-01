from flask import (
    Blueprint,
    render_template,
    request,
    flash,
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


@maintenance.route("/maintenance/reorder-locations", methods=["POST"])
def reorder_locations():
    data = request.get_json()
    id_order = data["id_order"]

    ordinal = 1
    for id in id_order:
        location = Location.query.filter_by(id=id).first()
        location.ordinal = ordinal
        db.session.commit()
        ordinal += 1

    return ""
