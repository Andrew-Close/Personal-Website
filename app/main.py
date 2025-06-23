from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .constants import STATIC_PATH

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html", static_path=STATIC_PATH)

@main.route("/bio")
def bio():
    return render_template("bio.html", static_path=STATIC_PATH)

@main.route("/projects")
def projects():
    return render_template("projects.html", static_path=STATIC_PATH)

@main.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", static_path=STATIC_PATH)