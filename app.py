from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from blueprints.task import task_blueprint
from blueprints.user import user_blueprint
import blueprints.user

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()

app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)
login_manager.login_view = 'user.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    blueprints.user.get_user(id=user_id)

app.register_blueprint(task_blueprint)
app.register_blueprint(user_blueprint)

app.app_context().push()
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)