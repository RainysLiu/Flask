from flask.blueprints import Blueprint

from flask import render_template

from tppapp.models import City

blue = Blueprint('blue',__name__)


@blue.route('/')
def index():
    citys = City.query.all()
    return render_template('index.html',**locals())




