from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user
from sqlalchemy import update

from database.database import db
from models.task import Task

task_blueprint = Blueprint('task', __name__)

def valid_dates(start_date, end_date):
    if start_date and start_date < datetime.today().date() or end_date and end_date < datetime.today().date():
        return 'Start date and end date cannot be in the past!'
    elif start_date and end_date and end_date < start_date:
        return 'End date cannot be before the start date!'
    return True

def convert_date(date):
    if date:
        return datetime.strptime(date, '%Y-%m-%d').date()
    return None

@task_blueprint.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('task/index.html', tasks=tasks)

@task_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = convert_date(str(request.form['start_date']))
        end_date = convert_date(str(request.form['end_date']))
        concluded = True if request.form.getlist('concluded') else False
        
        valid_date = valid_dates(start_date, end_date)
        if not title:
            flash('Title is required!')
        elif valid_date is not True:
            flash(valid_date)    
        else:
            task = Task(title=title, description=description, start_date=start_date, end_date=end_date, concluded=concluded, user_id=current_user.id)
            db.session.add(task)
            db.session.commit() 

            return redirect(url_for('task.index'))
    return render_template('task/create.html')


@task_blueprint.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id: int):
    task = Task.query.filter_by(id=id).first()

    if not task or task.id != current_user.id:
        return redirect(url_for('task.index'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = convert_date(request.form['start_date'])
        end_date = convert_date(request.form['end_date'])
        concluded = True if request.form.getlist('concluded') else False

        valid_date = valid_dates(start_date, end_date)
        if not title:
            flash('Title is required!')
        elif valid_date is not True:
            flash(valid_date)
        else:
            db.session.execute(update(Task).where(Task.id == id).values(title=title,description=description,start_date=start_date,end_date=end_date,concluded=concluded))
            db.session.commit()

            return redirect(url_for('task.index'))
    
    return render_template('task/edit.html', task=task)

@task_blueprint.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id: int):
    task = Task.query.filter_by(id=id).first()
    
    if not task or task.id != current_user.id:
        return redirect(url_for('task.index'))
    
    db.session.delete(task)
    db.session.commit()

    flash('"{}" was successfully deleted!'.format(task.title))
    return redirect(url_for('task.index'))