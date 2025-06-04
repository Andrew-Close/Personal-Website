from flask import Flask, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
# db = SQLAlchemy(app)

# class MessageModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     message = db.Column(db.String(875), nullable=False)
#     sender = db.Column(db.String(30), nullable=False)
#     date = db.Column(db.Date, nullable=False)

# with app.app_context():
#     db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("index.html")
    else:
        abort(405)

@app.route("/server-info")
def server_info():
    return render_template("server-info.html")

app.run()