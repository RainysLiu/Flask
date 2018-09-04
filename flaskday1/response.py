

from flask import Flask, redirect
from flask import make_response

app = Flask(__name__)

@app.route('/index')
def index():
    return '<h3>这是普通文本响应</h3>',300
@app.route('/response')
def return_response():
    response=make_response('<h3 style="color:red">这是个response响应</h3>')
    response.set_cookie('fruit','apple_cookie_value')
    return response

@app.route('/redirect')
def show_redirect():
    print('正在重定向到...')
    return redirect('/response')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

