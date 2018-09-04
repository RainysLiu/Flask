from flask import Blueprint,render_template

blue = Blueprint('blue',__name__)

@blue.route('/addstu')
def goaddstu():
    return render_template('addstu.html')
