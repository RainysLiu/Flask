from flask import Flask
from lantu.views import blue

def new_app():
    myapp = Flask(__name__)
    myapp.register_blueprint(blueprint=blue,url_prefix = '/lantu')
    return myapp


