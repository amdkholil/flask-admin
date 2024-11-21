from flask import Flask
from .config import Config
from .extensions import db, login_manager
from .routes.admin import init_admin
from  .models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register routes
    init_admin(app)
    

    return app

@login_manager.user_loader
def load_user(id):
    # Return the user object based on the user_id
    return User.query.get(id)