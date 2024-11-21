
from flask_admin import Admin, menu
from ..models.user import User, UserModelView
from ..extensions import db


# Initialize Flask-Admin and add views
def init_admin(app):
    app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
    admin = Admin(app, name='Admin', template_mode='bootstrap4')
    
    # Add logout link in the menu navbar
    admin.add_link(menu.MenuLink(name='Logout', url='/logout', icon_type='fa', icon_value='fa-sign-out'))
    
    # Add views
    admin.add_view(UserModelView(User, db.session))
    
