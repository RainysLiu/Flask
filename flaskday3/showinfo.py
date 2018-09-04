from flask import Flask,render_template
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/show/<name>')
def show_info(name):
    countrys = ['汉帝国','明帝国','唐帝国','秦帝国']
    clours = ['红色','黄色','蓝色','绿色']
    return render_template('showinfo.html',**locals())

if __name__ == '__main__':
    manager.run()


