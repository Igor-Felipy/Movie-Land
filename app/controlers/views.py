from . import controller
from flask import render_template, request
from app.models.tables import Video

@controller.route('/')
def index():
    return render_template('index.html')

@controller.route('/video/<int:id>/')
def video(id):
    video = Video.query.filter_by(id=id).first()
    return render_template('video.html',video=video)

@controller.route('/list/<list>/')
def list(list):
    return render_template('list.html')

@controller.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_data = request.form.get('search')
        search = "%{}%".format(search_data)
        found = Video.query.filter(Video.title.like(search)).all()
        return render_template('search.html',search=search,found=found)
