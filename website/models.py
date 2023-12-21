from . import db
from flask_login import UserMixin


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    venues = db.relationship("Venue")
    ordinal = db.Column(db.Integer)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    link = db.Column(db.String(300))
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    frequency = db.Column(db.String(150))
    genre = db.Column(db.String(150))
