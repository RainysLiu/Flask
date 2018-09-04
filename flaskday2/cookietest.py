from flask import Flask,make_response,request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/setcookie')
def set_cookie():
    response = make_response("<h3>cookies is set successfully!</h3>")
    response.set_cookie('fruit_cookie','apple') # add a cookie
    response.set_cookie('sport_cookie','football',max_age=60)
    return response

@app.route('/deletecookie')
def delete_cookie():
    response = make_response("<h3>fruit_cookie is deleted successfully!</h3>")
    response.delete_cookie('fruit_cookie')   # delete a cookie
    return response

@app.route('/getcookie')
def get_cookie():
    fruit_cookie = request.cookies.get("fruit_cookie")
    sport_cookie = request.cookies.get("sport_cookie")
    html = "<h3>fruit_cookie:%s</h3>"%fruit_cookie
    html += "<h3>sport_cookie:%s</h3>"%sport_cookie
    return html

if __name__ == '__main__':
    manager.run()
