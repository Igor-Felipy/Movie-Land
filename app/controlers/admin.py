from . import controller
from flask import render_template


@controller.route('/admin')
def admin():
    return render_template("admin_login.html")

