from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions here
db = SQLAlchemy()

login_manager = LoginManager()
