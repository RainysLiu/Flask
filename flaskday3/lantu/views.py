from flask import Blueprint,render_template
import os

blue = Blueprint("mylantu",__name__,)


@blue.route('/showinfo/<name>')
def show_info(name):
    countrys = ['中国', '日本', '韩国', '新加坡']
    clours = ['紫色', '青色', '黑色', '白色']
    return render_template('showinfo.html', **locals())






