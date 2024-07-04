from flask import Blueprint, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash

from database.database import get_connection
from blueprints.task import task_blueprint

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

        if len(password) <= 5:
            flash('The password must be at least 6 characters long!')
        elif user_exist(email):
            flash('User already exists!') 
        else:
            hash_password = generate_password_hash(password)

            conn = get_connection()
            conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hash_password))
            conn.commit()
            conn.close()       

            return redirect(url_for('task.index'))
    return render_template('user/register.html')