from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# from flask_login import current_user
from ..models.user import User
# from ..models.post import Post
from ..extensions import db

# Custom ModelView for User with restricted access
class UserModelView(ModelView):
    def is_accessible(self):
        # return current_user.is_authenticated and current_user.is_admin
        return True



# Initialize Flask-Admin and add views
def init_admin(app):
    admin = Admin(app, name='Admin', template_mode='bootstrap4')
    admin.add_view(UserModelView(User, db.session))
