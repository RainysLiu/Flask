
from flask import Flask
from homeworkapp.ext import init_ext


def create_app():
    app = Flask(__name__,)
    app.config['SECRET_KEY'] = '123456'
    init_ext(app)
    return app
