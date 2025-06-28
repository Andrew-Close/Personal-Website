from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .admin import admin as admin_blueprint

def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(admin_blueprint)
