from flask import Blueprint, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from database.database import db
from models.user import User

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        user = User.query.filter_by(email=email).first()

        if len(password) <= 5:
            flash('The password must be at least 6 characters long!')
        elif password != confirm_password:
            flash('Passwords must be the same!')
        elif user:
            flash('User already exists!')
        else:
            hash_password = generate_password_hash(password)

            new_user = User(name=name, email=email, password=hash_password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration completed successfully!')
            return redirect(url_for('user.login'))
    return render_template('user/register.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user=user, remember=remember)
            return redirect(url_for('task.index'))
        flash('Please check your login details and try again.')

    return render_template('user/login.html')

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))