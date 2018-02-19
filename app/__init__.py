from flask import Flask
from mongoengine import connect

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
connect(host=app.config['MONGODB_URI'])

from app import routes, models
