from . import controller
from app import db, lm
from flask import render_template, request, url_for, redirect, flash
from app.models.forms import Adm_form, New_adm_form, New_video_form
from app.models.tables import Adm, Video
from flask_login import login_user,logout_user,current_user

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@controller.route('/admin/', methods=['GET','POST'])
def admin():
    form = Adm_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Adm.query.filter_by(username=form.user.data).first()
            if user and user.password == form.password.data:
                login_user(user)
                return redirect(url_for('index'))
            else:
                #add a flash message
                return redirect(url_for(admin))
    else:
        return render_template("admin_login.html",form=form)

@controller.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("index"))


@controller.route('/new_admin',methods=['GET','POST'])
def new_admin():
    form = New_adm_form()
    if request.method == 'Post':
        if form.validate_on_submit():
            NewAdmData = Adm(form.user.data, form.password.data, form.power.data)
            db.session.add(NewAdmData)
            db.session.commit()
            return redirect(url_for('index')) #add a flash message
        else:
            pass #add a flash message
    else:
        return render_template("new_admin.html", form=form)


@controller.route('/new_movie', methods=['GET','POST'])
def new_movie():
    form = New_video_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            NewVideoData = Video(form.title.data,form.genre.data,form.serie.data,form.link.data,form.image.data)
            db.session.add(NewVideoData)
            db.session.commit()
            #add a flash message
            return redirect(url_for('new_movie'))
        else:
            pass#add a flash message
    else:
        return render_template('new_movie.html',form=form)