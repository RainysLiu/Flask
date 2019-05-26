
from tppapp.views import blue
from tppapp.api import api
def init_ext(app):
    app.register_blueprint(blueprint=blue)
    api.init_app(app)