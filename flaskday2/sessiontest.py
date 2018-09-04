from flask import Flask,session
from flask_script import Manager

app = Flask(__name__)
app.secret_key = '123456'  # set secret key to app
manager = Manager(app)

@app.route('/setsession')
def set_session():
    session['username'] = 'tom'
    session['home'] = 'China'
    session['hobby'] = 'football'
    return '<h3>set session successful!</h3>'

@app.route('/del/<key>')
def delete_session(key):
    session.pop(key)
    return 'delete %s key successful'%key

@app.route('/delall')
def delete_all():
    session.clear()
    return 'delete all session key->value successful'

@app.route('/show/all')
def show_all():
    html = ''
    for k,v in session.items():
        html += k
        html += "========>"
        html += v
        html += '<hr/>'
    return html

if __name__ == '__main__':
    manager.run()



