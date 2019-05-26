from flask import Flask
from tppapp.models import db
from tppapp.settings import Config
from tppapp.ext import init_ext

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    init_ext(app)
    db.init_app(app)
    return app
