from app import db

class Adm(db.Model):
    __tablename__="adms"
    id = db.Column(db.Integer, prymary_key=True)
    username = db.Column(db.String(40),unique=True, nullable=False)
    password = db.Column(db.String(40),unique=True, nullable=False)
    def __init__(self, username, password)
        self.username = username
        self.password = password


class Video(db.Model):
    __tablename__="videos"
    id = db.Column(db.Integer, prymary_key=True)
    title = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(50), nullable=False)
    serie_title = db.Column(db.String(120))
    link = db.Column(db.String(140), nullable=False)
    def __init__(self,title,genres,serie_title,link)
        self.title = title
        self.genres = genres
        self.serie_title = serie_title
        self.link = link


class Coments(db.Model):
    __tablename__="Coments"
    id = db.Column(db.Integer, prymary_key=True)
    coment = db.Column(db.Integer)
    def __init__(self,coment):
        self.coment = coment