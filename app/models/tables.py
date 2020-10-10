from app import db

class Adm(db.Model):
    __tablename__="adms"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40),unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    power = db.Column(db.Integer, nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password,power):
        self.username = username
        self.password = password
        self.power = power


class Video(db.Model):
    __tablename__="videos"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(50), nullable=False)
    serie_title = db.Column(db.String(120))
    link = db.Column(db.String(140), nullable=False)
    image = db.Column(db.String(200),nullable=False)
    
    def __init__(self,title,genres,serie_title,link,image):
        self.title = title
        self.genres = genres
        self.serie_title = serie_title
        self.link = link
        self.image = image


class Coments(db.Model):
    __tablename__="Coments"
    
    id = db.Column(db.Integer, primary_key=True)
    coment = db.Column(db.Integer)
    
    def __init__(self,coment):
        self.coment = coment