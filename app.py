from flask import Flask
from decouple import config

from blueprints.task import task_blueprint
from blueprints.user import user_blueprint

app = Flask(__name__)

app.register_blueprint(task_blueprint)
app.register_blueprint(user_blueprint)

app.config['SECRET_KEY'] = config('SECRET_KEY')

if __name__ == '__main__':
    app.run(debug=True)