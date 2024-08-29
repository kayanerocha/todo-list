from sqlalchemy import TIMESTAMP
import datetime

from database.database import db

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    concluded = db.Column(db.Boolean)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, title, description, start_date, end_date, concluded, user_id) -> None:
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.concluded = concluded
        self.user_id = user_id
        