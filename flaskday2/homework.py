from flask import Flask, session, render_template
from flask_script import Manager

app = Flask(__name__)
app.secret_key = '123456'  # set secret key to app
manager = Manager(app)

#登录验证
@app.route('/login/<username>/<pwd>')
def reaction(username,pwd):
    if username=='tom' and pwd=='123456':
        session['username'] = username
        session['password'] = pwd
        return '<h3> 恭喜登录成功!</h3>'
    else:
        return '<h3> 用户名或密码输入错误!</h3>'
#宏的石用
@app.route('/hong')
def use_macro():
    return render_template('usehong.html', poples={'姓名':'人生导师贺磊磊','年龄':25, '性别':'男'})

#自定义错误处理

@app.errorhandler(500)
def error_500(e):
    return render_template('error500.html',error='ZeroDivisionError: division by zero')

@app.route('/compute')
def compute():
    i = 5 / 0
    return '结果成功'

if __name__ == '__main__':
    manager.run()



