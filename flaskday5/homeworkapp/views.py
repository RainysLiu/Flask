
from flask import Blueprint, request, jsonify
from flask import render_template

from homeworkapp.models import *

blue = Blueprint("blue",__name__)



#首页
@blue.route('/startui')
def startui():
    return render_template("startui.html")


#查看所有学生信息
@blue.route('/getallstu')
def getallstu():
    students = Student.query.all()
    return render_template("allstu.html",**locals())
#添加学生信息
@blue.route('/goaddstu')
def goaddstu():
    clses = Class.query.all()
    return render_template("addstudent.html",**locals())
@blue.route('/addstu',methods=['GET', 'POST'])
def addstu():
    n = request.form["stuName"]
    a = request.form["stuAge"]
    se = request.form["sex"]
    sc= int(request.form["score"])
    cid = request.form["classes"]
    print(n,a,se,sc,cid)
    newstu = Student(name=n,age=a,sex=se,score=sc,class_id=int(cid))
    db.session.add(newstu)
    return render_template("addstudentok.html",**{'n':n})





#查看所有班级信息
@blue.route('/getallcls')
def getallcls():
    clses = Class.query.all()
    return render_template("allcls.html",**locals())
#添加班级
@blue.route('/goaddcls')
def goaddcls():
    return render_template("addcls.html")
@blue.route('/addcls',methods=['GET', 'POST'])
def addcls():
    n = request.form["clsName"]
    clses = Class.query.all()
    clsnamelist = []
    for cls in clses:
        clsnamelist.append(cls.name)
    if n in clsnamelist:
        return render_template('addcls.html',**{'msg':'班级名已存在！'})
    else:
        newcls = Class(name=n)
        db.session.add(newcls)
        return render_template("addclsok.html",**{'n':n})



#修改学生信息
@blue.route('/gomodstu')
def gomodstu():
    students = Student.query.all()
    clses = Class.query.all()
    return render_template("modstu.html",**locals())
@blue.route('/modstu',methods=['GET', 'POST'])
def modstu():
    n = request.form["stuName"]
    a = request.form["stuAge"]
    se = request.form["sex"]
    sc = int(request.form["score"])
    cid = request.form["classes"]
    print(n, a, se, sc, cid)
    selected_id= int(request.form["sel_stu"])
    stu = Student.query.get(selected_id)
    stu.name = n
    stu.age = a
    stu.sex = se
    stu.score = sc
    stu.class_id = cid
    db.session.commit()
    return render_template("modstuok.html",**{'n': n})
@blue.route('/getstu/<stuid>',methods=['GET', 'POST'])
def getstu(stuid):
    stu = Student.query.get(int(stuid))
    stus = {'name':stu.name,'age':stu.age,'score':stu.score,'sex':stu.sex,'cls':stu.cls.name}
    print('查询学生成功')
    return jsonify(stus)


#删除学生信息
@blue.route('/godelstu')
def godelstu():
    students = Student.query.all()
    return render_template("deletestu.html",**locals())
@blue.route('/delstu',methods=['GET', 'POST'])
def delstu():
    n = request.form["stuname"]
    Student.query.filter_by(name=n).delete()
    return render_template("deletestuok.html",**{'n':n})





