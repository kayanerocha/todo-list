from sqlalchemy import TIMESTAMP
from flask_login import UserMixin
import datetime

from database.database import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    tasks = db.relationship('Task', backref='user')