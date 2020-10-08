from . import controller
from flask import render_template

@controller.route('/')
def index():
    return render_template("index.html")

@controller.route('/video/<int:id>')
def video(id):
    return render_template('video.html')

@controller.route('/list/<list>')
def list(list):
    return render_template('list.html')