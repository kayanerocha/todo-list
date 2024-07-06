from app import db
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, Double, Date, DateTime, Pri
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())

