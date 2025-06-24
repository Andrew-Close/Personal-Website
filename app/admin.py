from flask import Blueprint, render_template, request, url_for, redirect, current_app
from flask_login import login_user, logout_user, login_required, current_user
from PIL import Image
from PIL.ExifTags import TAGS
from werkzeug.security import check_password_hash
from .extensions import db
from .models import UserModel, ImageModel, LocationModel
from .constants import STATIC_PATH
from .table_managers.images_manager import ImagesManager
import os.path
from datetime import datetime

def get_all_unstored_photos():
    image_manager = ImagesManager()
    all_images = os.listdir("app/static/portfolio-images")
    all_stored_images = image_manager.select_all_images()
    for stored_image in all_stored_images:
        for image_name in all_images:
            if stored_image.image_name == image_name:
                all_images.remove(stored_image.image_name)
                break
    all_images = sorted(all_images, key=lambda name: get_name_number(name))
    return all_images

admin = Blueprint("admin", __name__)
unstored_photos = []

@admin.route("/admin-panel")
@login_required
def admin_panel():
    global unstored_photos
    unstored_photos = get_all_unstored_photos()
    return render_template("admin-panel.html")

@admin.route("/admin-panel/manage-photos")
@login_required
def manage_photos():
    return render_template("manage-photos.html")

@admin.route("/admin-panel/manage-photos/add-photos", methods=["GET", "POST"])
@login_required
def add_photos():
    image_name = unstored_photos[0]
    all_locations = db.session.execute(db.select(LocationModel)).scalars().all()
    if request.method == "POST":
        rank = request.form.get("rank")
        location = request.form.get("location")

        location_obj = db.session.execute(db.select(LocationModel).where(LocationModel.location == location)).scalars().first()
        if not location_obj:
            location_obj = LocationModel(location=location)

        date = None
        exif = Image.open("app/static/portfolio-images/{}".format(image_name))._getexif()
        for tagid in exif:
            tagname = TAGS.get(tagid, tagid)
            if tagname == "DateTimeOriginal":
                date = exif.get(tagid)
                break
        if date is not None:
            date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")

        image = ImageModel(image_name=image_name, rank=rank, date=date, location=location_obj)
        db.session.add(image)
        db.session.commit()
        unstored_photos.pop(0)
        return redirect(url_for("admin.add_photos"))
    return render_template("add-photos.html", image_name=image_name, locations=all_locations)

def get_name_number(name):
    starting_index = -1
    for i in range(len(name)):
        if name[i].isdigit():
            if starting_index == -1:
                starting_index = i
        else:
            if not starting_index == -1:
                ending_index = i
                return int(name[starting_index:ending_index])
    raise Exception("Something went wrong in get_name_number")