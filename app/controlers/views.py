from . import controller
from flask import render_template, request, redirect, url_for
from app.models.tables import Video

@controller.route('/')
def index():
    videos = Video.query.order_by(Video.id.desc()).limit(20)
    return render_template('index.html',videos=videos)

@controller.route('/video/<int:id>/')
def video(id):
    video = Video.query.filter_by(id=id).first()
    return render_template('video.html',video=video)

@controller.route('/list/')
def list():
    videos = Video.query.all()
    return render_template('list.html',videos=videos)

@controller.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_data = request.form.get("search") 
        search = "%{}%".format(search_data)
        found = Video.query.filter(Video.title.like(search)).all()
        return render_template('search.html',search_data=search_data,found=found)
    else:
        return redirect(url_for("index.html"))