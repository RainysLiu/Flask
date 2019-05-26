from flask import Flask

from homework.ext import init_ext
from homework.models import db
from homework.settings import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    init_ext(app)
    db.init_app(app)
    return app


