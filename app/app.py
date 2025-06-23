from flask import Flask, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object("config")
# db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bio")
def bio():
    return render_template("bio.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

app.run()