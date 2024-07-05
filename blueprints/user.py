from flask import Blueprint, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash

from database.database import get_connection

user_blueprint = Blueprint('user', __name__)

def user_exist(email):
    conn = get_connection()
    user = conn.execute('SELECT * FROM users where email = ?', (email,)).fetchone()
    conn.close()

    if user:
        return True
    return False

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if len(password) <= 5:
            flash('The password must be at least 6 characters long!')
        elif password != confirm_password:
            flash('Passwords must be the same!')
        elif user_exist(email):
            flash('User already exists!')
        else:
            hash_password = generate_password_hash(password)

            conn = get_connection()
            conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hash_password))
            conn.commit()
            conn.close()

            flash('Registration completed successfully!')
            return redirect(url_for('user.login'))
    return render_template('user/register.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('user/login.html')