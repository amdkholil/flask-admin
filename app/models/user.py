from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from ..extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Enum("admin", "user"), nullable=False, default="user")
    photo = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.name} {self.email} {self.role} {self.photo}>"

    def set_password(self, password):
        """Hash the password before saving."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)
    
    def isAdmin(self):
        return self.role == "admin"


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


# Custom ModelView for User with restricted access
class UserModelView(ModelView):
    column_searchable_list = ["name", "email", "role", "photo"]
    column_exclude_list = ["password"]
    can_export = True
    page_size = 10
    can_set_page_size = True
    can_view_details = True

    def create_model(self, form):
        user = User(
            name=form.name.data,
            email=form.email.data,
            role=form.role.data,
            photo=form.photo.data,
            password=generate_password_hash(form.password.data),
        )
        db.session.add(user)
        db.session.commit()
        return user

    def update_model(self, form, model):
        if(form.name.data):
            model.name = form.name.data
        if(form.email.data):
            model.email = form.email.data
        if(form.photo.data):
            model.photo = form.photo.data
        if(form.role.data):
            model.role = form.role.data
        if(form.password.data):
            model.password = generate_password_hash(form.password.data)
            
        db.session.commit()
        return model

    def is_accessible(self):
        return current_user.is_authenticated and current_user.isAdmin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin.index"))
