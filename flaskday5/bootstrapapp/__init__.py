from flask import Flask
from flask_bootstrap import Bootstrap
from bootstrapapp.views import blue


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.register_blueprint(blueprint=blue)
    return app
