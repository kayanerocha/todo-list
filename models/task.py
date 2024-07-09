from sqlalchemy import TIMESTAMP
import datetime

from database.database import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    concluded = db.Column(db.Boolean)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
        