from flask_restful import Resource,Api
from flask import request, Flask, render_template, redirect

from restapp.views import blue

students_dic = {
    '1':{'name':'贺磊磊','age':20,'score':88},
    '2':{'name':'习近平','age':50,'score':100},
    '3':{'name':'特朗普','age':50,'score':86},
}


app = Flask(__name__)
app.register_blueprint(blueprint=blue)
api = Api(app)






class Student(Resource):  #继承了restful类
    def get(self):  #如果是get请求
        return students_dic
    def post(self):
        stuname = request.form["stuname"]
        stuage = request.form['stuage']
        stuscore = request.form['stuscore']
        new_stu = {'name':stuname,'age':stuage,'score':stuscore}
        new_stuid = int(max(students_dic.keys())) +1
        students_dic[str(new_stuid)]=new_stu
        print('添加成功，现在所有的学生数据是：',students_dic)
        return redirect('/student')


api.add_resource(Student,'/student')


