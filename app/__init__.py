from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='templates')
app.config.from_object('config')

db = SQLAlchemy(app)

from app.controlers import controller
app.register_blueprint(controller)