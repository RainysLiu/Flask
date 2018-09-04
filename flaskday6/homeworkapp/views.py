from flask import Blueprint, session, flash, redirect, url_for, request, jsonify
from flask import render_template


from homeworkapp.forms import User

blue = Blueprint("blue",__name__)




@blue.route('/login',methods=['GET','POST'])
def login():
    form = User()
    if form.validate_on_submit():
        print('表单已经验证通过')
        if form.name.data=='tom' and form.password.data=='123456':
            print('账户密码验证成功')
            session["name"] = form.name.data
            return redirect(url_for('blue.success')) # 重定向发送GET请求，url_for()反向解析URL
        else:
            flash('用户名或密码错误')
            return redirect(url_for('blue.login'))
    return render_template('login.html', form=form)
@blue.route('/success',methods=['GET','POST'])
def success():
    return render_template('success.html',name=session.get("name"))




@blue.route('/showinfo',methods=['GET','POST'])
def index():
    return render_template('showinfo.html')

@blue.route('/getinfo/<info>',methods=['GET','POST'])
def fruit(info):
    if info == '水果':
        print('成功查询水果')
        return jsonify([{'name':'草莓','price':10.8},{'name':'香蕉','price':8.8},{'name':'苹果','price':16.8}])
    elif info == '运动':
        print('成功查询运动')
        return jsonify([{'name': '篮球', 'price': 67.9 },{'name': '足球', 'price': 97.9 },{'name': '排球', 'price': 87.9 },])
    else:
        print('没有该商品')
        return jsonify('none')

@blue.route('/picNmov')
def picNmov():
    return render_template('picNmov.html')





