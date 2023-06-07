from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    describtion = TextAreaField('describtion', validators=[DataRequired()])
    done = BooleanField('done', validators=[DataRequired()])

