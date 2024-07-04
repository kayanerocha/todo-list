from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime

from database.database import get_connection

task_blueprint = Blueprint('task', __name__)

def get_task(id: int):
    conn = get_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?;', (id,)).fetchone()
    conn.close()
    return task

def valid_dates(start_date, end_date):
    if start_date and datetime.strptime(start_date, '%Y-%m-%d').date() < datetime.today().date() or end_date and datetime.strptime(end_date, '%Y-%m-%d').date() < datetime.today().date():
        return 'Start date and end date cannot be in the past!'
    elif start_date and end_date and datetime.strptime(end_date, '%Y-%m-%d') < datetime.strptime(start_date, '%Y-%m-%d'):
        return 'End date cannot be before the start date!'
    return True

@task_blueprint.route('/')
def index():
    conn = get_connection()
    tasks = conn.execute('SELECT * FROM tasks;').fetchall()
    conn.close()
    return render_template('task/index.html', tasks=tasks)

@task_blueprint.route('/<int:id>')
def task(id: int):
    task = get_task(id)
    return render_template('task/task.html', task=task)

@task_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        concluded = 1 if request.form.getlist('concluded') else 0
        
        valid_date = valid_dates(start_date, end_date)
        if not title:
            flash('Title is required!')
        elif valid_date is not True:
            flash(valid_date)      
        else:
            conn = get_connection()
            conn.execute('''INSERT INTO tasks (title, description, start_date, end_date, concluded)
                         VALUES (?, ?, ?, ?, ?);''', (title, description, start_date, end_date, concluded))
            conn.commit()
            conn.close()
            return redirect(url_for('task.index'))
    return render_template('task/create.html')


@task_blueprint.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id: int):
    task = get_task(id)
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        concluded = 1 if request.form.getlist('concluded') else 0

        valid_date = valid_dates(start_date, end_date)
        if not title:
            flash('Title is required!')
        elif valid_date is not True:
            flash(valid_date)
        else:
            conn = get_connection()
            conn.execute('''UPDATE tasks
                         SET title = ?, description = ?, start_date = ?, end_date = ?, concluded = ?
                         WHERE id = ?;''', (title, description, start_date, end_date, concluded, id))
            conn.commit()
            conn.close()
            return redirect(url_for('task.index'))
    
    return render_template('task/edit.html', task=task)

@task_blueprint.route('/<int:id>/delete', methods=['POST'])
def delete(id: int):
    task = get_task(id)
    conn = get_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?;', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(task['title']))
    return redirect(url_for('task.index'))