import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-my-secret-key'
    MONGODB_URI = os.environ.get(
        'DB_CONN') or 'mongodb://user:password@ds239648.mlab.com:39648/flask_forum'
