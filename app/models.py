from flask_login import UserMixin
from .extensions import db

class UserModel(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class ImageModel(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(15), nullable=False)
    rank = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    location = db.relationship("LocationModel", back_populates="images")

class LocationModel(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    images = db.relationship("ImageModel", back_populates="location")