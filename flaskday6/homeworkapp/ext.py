from flask_bootstrap import Bootstrap

from homeworkapp.views import blue



def init_ext(app):
    app.register_blueprint(blueprint=blue)
    Bootstrap(app)

