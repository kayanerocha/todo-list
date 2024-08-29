from decouple import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

conn = f'mysql+pymysql://{config("MYSQL_USER")}:{config("MYSQL_PASSWORD")}@{config("MYSQL_HOST")}/{config("MYSQL_DATABASE")}'