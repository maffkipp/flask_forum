from app import app, db
from flask import render_template, redirect, url_for, request
from app.models import Comment, Post, CommentForm, PostForm


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('posts'))


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm(request.form)
    posts = Post.objects()
    if request.method == 'POST' and form.validate():
        new_post = Post(title=form.title.data)
        new_post.content = form.content.data or ''
        new_post.name = form.name.data or 'anonymous_user'
        new_post.save()
        return redirect(url_for('posts'))
    return render_template('index.html', form=form, posts=posts)
