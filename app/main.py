from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .constants import STATIC_PATH

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