from app.api import api



def init_ext(app):
    api.init_app(app)
