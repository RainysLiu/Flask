from flask import Flask
from flask_script import Manager

app = Flask(__name__)  # 实例化"程序实例”
manager = Manager(app)  # 将app实例化对象传入Manager构造方法中


@app.route('/')
def show():
    return "<h3 style='color:blue'>使用了flask-script插件,hahahaha...</h3>"


if __name__ == '__main__':
    manager.run()






