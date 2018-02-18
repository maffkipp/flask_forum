from flask import Flask
from mongoengine import *

connect(host='mongodb://user:password@ds239648.mlab.com:39648/flask_forum')

app = Flask(__name__)

from app import routes
