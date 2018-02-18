from app import app
from models import Comment, Post


@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
