from flask import Flask
from .extensions import db, login_manager
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_PATH = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_PATH, exist_ok=True)
DB_PATH = os.path.join(INSTANCE_PATH, "database.db")

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    app.config["SECRET_KEY"] = "secret-key"

    db.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import UserModel

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.execute(db.select(UserModel).where(UserModel.id == user_id)).scalars().first()

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app