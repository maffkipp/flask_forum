from app import app
from flask import render_template, redirect, url_for, request
from app.models import Comment, Post
from app.forms import PostForm, CommentForm


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('posts'))


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title)
        new_post.content = form.content or ''
        new_post.name = form.name or 'anonymous_user'
        new_post.save()
        print('saved post to db')
        return redirect(url_for('posts'))
    return render_template('index.html', form=form, posts=Post.objects)
