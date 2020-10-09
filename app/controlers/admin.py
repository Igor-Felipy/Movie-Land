from . import controller
from flask import render_template


@controller.route('/admin')
def admin():
    return render_template("admin_login.html")

@controller.route('/new_admin')
def new_admin():
    return render_template("new_admin.html")

@controller.route('/new_movie')
def new_movie():
    return render_template('new_movie.html')