from cacheapp.views import cache,blue
from flask import Flask



def createapp():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    cache.init_app(app)
    return app

