from app import app
from flask import render_template
from app.models import Comment, Post
from app.forms import PostForm, CommentForm


@app.route('/')
@app.route('/index')
def index():
    form = PostForm()
    return render_template('index.html', form=form)
