from flask import Flask
from .extensions import db, login_manager
from .blueprints import register_blueprints
from .constants import INSTANCE_PATH, DB_PATH
import os

os.makedirs(INSTANCE_PATH, exist_ok=True)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    app.config["SECRET_KEY"] = "secret-key"

    db.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import UserModel, ImageModel

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.execute(db.select(UserModel).where(UserModel.id == user_id)).scalars().first()

    register_blueprints(app)

    print("Before deletion")
    with app.app_context():
        all_images = db.session.execute(db.select(ImageModel)).scalars().all()
        for image in all_images:
            db.session.delete(image)
        db.session.commit()

    return app