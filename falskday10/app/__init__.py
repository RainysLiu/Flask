from flask import Flask

from app.ext import init_ext
from app.models import db

from app.settings import Config





def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    init_ext(app)
    return app


print(Config().SQLALCHEMY_DATABASE_URI)



