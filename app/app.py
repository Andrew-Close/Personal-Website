from flask import Flask, render_template, app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/server-info")
def server_info():
    return render_template("server-info.html")

app.run()