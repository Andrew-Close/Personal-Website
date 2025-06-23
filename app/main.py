from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/bio")
def bio():
    return render_template("bio.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@main.route("/admin-panel")
@login_required
def admin_panel():
    return render_template("admin-panel.html", name=current_user.name)