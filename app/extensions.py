from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions here
db = SQLAlchemy()

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import get_user_by_id
    return get_user_by_id(user_id)
