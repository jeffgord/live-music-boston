from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from .. import db
from ..models import Location, Venue


maintenance = Blueprint("maintenance", __name__)


@maintenance.route("/maintenance")
@login_required
def page():
    locations = Location.query.all()
    venues = Venue.query.all()
    return render_template("maintenance.html", locations=locations, venues=venues)


@maintenance.route("maintenance/add-location", methods=["POST"])
@login_required
def add_location():
    name = request.form["name"]

    if Location.query.filter_by(name=name).first():
        flash("A location already exists with that name!")
    else:
        new_location = Location(name=name)
        db.session.add(new_location)
        db.session.commit()

    return redirect(url_for("maintenance.page"))


@maintenance.route("maintenance/delete-location", methods=["POST"])
@login_required
def delete_location():
    location_id = request.form["location_id"]
    location = Location.query.filter_by(id=location_id).first()

    if not location:
        flash("Location does not exist!")
    else:
        db.session.delete(location)
        db.session.commit()

    return redirect(url_for("maintenance.page"))


@maintenance.route("maintenance/edit-location", methods=["POST"])
@login_required
def edit_location():
    location_id = request.form["location_id"]
    location = Location.query.filter_by(id=location_id).first()

    if not location:
        flash("Location does not exist!")
    else:
        new_name = request.form["name"]
        location.name = new_name
        db.session.commit()

    return redirect(url_for("maintenance.page"))


@maintenance.route("maintenance/add-venue", methods=["POST"])
@login_required
def add_venue():
    name = request.form["name"]
    link = request.form["link"]
    location_id = request.form["location_id"]
    frequency = request.form["frequency"]
    genre = request.form["genre"]

    if Venue.query.filter_by(name=name).first():
        flash("A Venue already exists with this name!")
    else:
        new_venue = Venue(
            name=name,
            link=link,
            location_id=location_id,
            frequency=frequency,
            genre=genre,
        )
        db.session.add(new_venue)
        db.session.commit()

    return redirect(url_for("maintenance.page"))


@maintenance.route("maintenance/delete-venue", methods=["POST"])
@login_required
def delete_venue():
    venue_id = request.form["venue_id"]
    venue = Venue.query.filter_by(id=venue_id).first()

    if not venue:
        flash("Venue does not exist!")
    else:
        db.session.delete(venue)
        db.session.commit()

    return redirect(url_for("maintenance.page"))


@maintenance.route("maintenance/edit-venue", methods=["POST"])
@login_required
def edit_venue():
    venue_id = request.form["venue_id"]
    venue = Venue.query.filter_by(id=venue_id).first()

    if not venue:
        flash("This venue does not exist!")
    else:
        venue.name = request.form["name"]
        venue.link = request.form["link"]
        venue.location_id = request.form["location_id"]
        venue.frequency = request.form["frequency"]
        venue.genre = request.form["genre"]
        db.session.commit()

    return redirect(url_for("maintenance.page"))
