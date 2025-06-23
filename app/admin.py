import os.path

from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from PIL import Image
from PIL.ExifTags import TAGS
from werkzeug.security import check_password_hash
from .extensions import db
from .models import UserModel
from .constants import STATIC_PATH

admin = Blueprint("admin", __name__)

@admin.route("/admin-panel")
@login_required
def admin_panel():
    return render_template("admin-panel.html")

@admin.route("/admin-panel/manage-photos")
@login_required
def manage_photos():
    return render_template("manage-photos.html")

@admin.route("/admin-panel/manage-photos/add-photos")
@login_required
def add_photos():
    all_images = os.listdir("app/static/portfolio-images")
    for name in all_images:
        exif = Image.open("app/static/portfolio-images/{}".format(name))._getexif()
        date = None
        for tagid in exif:
            tagname = TAGS.get(tagid, tagid)
            if tagname == "DateTimeOriginal":
                date = exif.get(tagid)
                break
    return render_template("add-photos.html", image_name="image1.jpg")