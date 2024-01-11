from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required
from sqlalchemy import func
from .. import db
from ..models import Location, Venue
from ..utils import json_message


maintenance = Blueprint("maintenance", __name__)


@maintenance.route("/maintenance")
@login_required
def page():
    return render_template("maintenance.html")


@maintenance.route("/maintenance/locations")
def locations():
    try:
        locations = list(Location.query.all())
        locations.sort(key=lambda location: location.ordinal)

        data = []
        for location in locations:
            data.append({"id": location.id, "name": location.name})

        return jsonify(data)
    except:
        return json_message.error()


@maintenance.route("/maintenance/add-location", methods=["POST"])
def add_location():
    try:
        name = request.form["name"]

        if Location.query.filter_by(name=name).first():
            return json_message.error("A location already exists with that name!")
        else:
            max_ordinal = db.session.query(func.max(Location.ordinal)).scalar()
            new_location = Location(name=name, ordinal=max_ordinal + 1)
            db.session.add(new_location)
            db.session.commit()

        return json_message.success("Added location")
    except:
        return json_message.error()


@maintenance.route("/maintenance/delete-location", methods=["POST"])
def delete_location():
    try:
        id = request.form["id"]
        location = Location.query.filter_by(id=id).first()

        if len(location.venues):
            return json_message.error(
                f"You must delete all associated venues before deleting location: {location.name}"
            )
        else:
            db.session.delete(location)
            db.session.commit()
    except:
        return json_message.error()


@maintenance.route("/maintenance/reorder-locations", methods=["POST"])
def reorder_locations():
    try:
        data = request.get_json()
        id_order = data["id_order"]

        ordinal = 1
        for id in id_order:
            location = Location.query.filter_by(id=id).first()
            location.ordinal = ordinal
            db.session.commit()
            ordinal += 1

        return json_message.success()
    except:
        return json_message.error()
