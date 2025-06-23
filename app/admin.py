from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from .extensions import db
from .models import UserModel
from .constants import STATIC_PATH

admin = Blueprint("admin", __name__)

@admin.route("/admin-panel")
@login_required
def admin_panel():
    return render_template("admin-panel.html",  static_path=STATIC_PATH)

@admin.route("/admin-panel/manage-photos")
@login_required
def manage_photos():
    return render_template("manage-photos.html",  static_path=STATIC_PATH)

@admin.route("/admin-panel/manage-photos/add-photos")
@login_required
def add_photos():
    return render_template("add-photos.html",  static_path=STATIC_PATH)