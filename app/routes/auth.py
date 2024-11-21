from flask import render_template, request, redirect, url_for, blueprints
from flask_login import login_user, logout_user, current_user
from app.viewmodels.login_viewmodel import LoginViewModel

authBp = blueprints.Blueprint('login', __name__)

@authBp.route('/login', methods=['GET', 'POST'])
def login():
    view_model = LoginViewModel()
    if request.method == 'POST':
        view_model.email = request.form['email']
        view_model.password = request.form['password']
        
        user = view_model.validate_user()
        
        if(user):
            login_user(user, remember=request.form.get('remember', False))
            return redirect(url_for('admin.index'))
        else:
            return render_template('auth/login.html', error=view_model.error_message)

    else:
        if(current_user.is_authenticated and current_user.isAdmin()):
            return redirect(url_for('admin.index'))
        return render_template('auth/login.html')

@authBp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login'))
