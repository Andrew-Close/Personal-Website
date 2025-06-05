from flask import Flask, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

class MessageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(875), nullable=False)
    sender = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date, nullable=False)
    string_date = db.Column(db.String(40), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        all_messages = db.session.execute(db.select(MessageModel).order_by(MessageModel.id)).scalars().all()
        all_messages.reverse()
        return render_template("index.html", all_messages=all_messages)
    elif request.method == "POST":
        message = request.form.get("message")
        sender = request.form.get("sender")
        date = datetime.now()
        string_date = datetime.strftime(date, "%B %#d, %Y, %#I:%M:%S %p")
        message_model = MessageModel(message=message, sender=sender, date=date, string_date=string_date)
        db.session.add(message_model)
        db.session.commit()

        all_messages = db.session.execute(db.select(MessageModel).order_by(MessageModel.id)).scalars().all()
        all_messages.reverse()
        return render_template("index.html", all_messages=all_messages)
    else:
        abort(405)

@app.route("/server-info")
def server_info():
    return render_template("server-info.html")

app.run()