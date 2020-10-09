from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class Adm(FlaskForm):
    username = StringField('user', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class Video(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    serie_title = StringField('serie', validators=[DataRequired()])
    link = StringField('link', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])

class Coment(FlaskForm):
    coment = TextAreaField('coment', validators=[DataRequired()])
