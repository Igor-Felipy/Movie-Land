from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__,template_folder='templates')
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager(app)

from app.controlers import controller
app.register_blueprint(controller)