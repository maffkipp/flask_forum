from app import app, db
from flask import render_template, redirect, url_for, request
from app.models import Comment, Post, CommentForm, PostForm
from datetime import datetime


@app.route('/')
@app.route('/index')
# base url and index redirect to posts
def index():
    return redirect(url_for('posts'))


@app.route('/posts', methods=['GET', 'POST'])
# route for viewing all posts, adding new posts
def posts():
    form = PostForm(request.form)
    posts = Post.objects()
    if request.method == 'POST' and form.validate():
        new_post = Post(title=form.title.data)
        new_post.content = form.content.data or ''
        new_post.name = form.name.data or 'anonymous_user'
        new_post.time = datetime.utcnow()
        new_post.save()
        return redirect(url_for('posts'))
    return render_template('index.html', form=form, posts=posts)


@app.route('/posts/<postid>', methods=['GET', 'POST'])
# route for viewing comments on one post, adding a new comment
def comments(postid):
    post = Post.objects(id=postid).first()
    form = CommentForm(request.form)
    if request.method == 'POST' and form.validate():
        new_comment = Comment(content=form.content.data)
        new_comment.name = form.name.data or 'anonymous_user'
        new_comment.time = datetime.utcnow()
        post.comments.append(new_comment)
        post.save()
        return redirect(url_for('comments', postid=postid))
    return render_template('comments.html', form=form, post=post)

