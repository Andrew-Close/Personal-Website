from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from .extensions import db
from .models import UserModel

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        user = db.session.execute(db.select(UserModel).where(UserModel.name == name)).scalars().first()
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for("auth.login"))
        login_user(user)
        return redirect(url_for("main.admin_panel"))
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))