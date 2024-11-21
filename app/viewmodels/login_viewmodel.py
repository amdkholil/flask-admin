from app.models.user import get_user_by_email
from werkzeug.security import check_password_hash

class LoginViewModel:
    def __init__(self):
        self.email = None
        self.password = None
        self.error_message = None

    def validate_user(self):
        user = get_user_by_email(self.email)
        if user and check_password_hash(user.password, self.password):
            return user
        else:
            self.error_message = "Invalid username or password"
            return None
