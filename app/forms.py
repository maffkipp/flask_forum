from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content')
    name = StringField('Name', validators=[Length(min=0, max=50)])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    content = StringField('Content')
    name = StringField('Name', validators=[Length(min=0, max=50)])
