from flask import Blueprint, session, flash, redirect, url_for
from flask import render_template

from wtfapp.forms import ProductForm

blue = Blueprint("blue",__name__)




@blue.route('/product',methods=['GET','POST'])
def product():
    form = ProductForm()
    if form.validate_on_submit():
        print("进入form.validate_on_submit()。。。")
        if form.proname.data != session['name']:  # 如果本次的数据与上次提交的不一样
             flash("哎呦，这次怎么不一样了？？？")
        session["name"] = form.proname.data  # 将表单数据存储于session中
        return redirect(url_for('blue.product'))  # 重定向发送GET请求，url_for()反向解析URL

    return render_template('login.html', name=session.get("name"), form=form)








