from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy

import blueprints
from blueprints.task import task_blueprint
from blueprints.user import user_blueprint

app = Flask(__name__)
db = SQLAlchemy()

app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)
# blueprints.login_manager.init_app(app)

app.register_blueprint(task_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)