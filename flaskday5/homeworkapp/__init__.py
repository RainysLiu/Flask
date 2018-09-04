
from homeworkapp.settings import app
from homeworkapp.views import blue



def createapp():
    app.register_blueprint(blueprint=blue)
    return app



