from flask_restful import Resource, Api


api = Api()

from homework.models import *



class getStudents(Resource):
    def get(self,stuid=None):
        if stuid:
            stu = Student.query.get(stuid)
            if stu:
                student = {"名字":stu.name,'性别': stu.sex, '年龄': stu.age, '分数': stu.score, '班级': stu.cls.name}
                return student
            else:
                return '该生不存在！'
        else:
            students = Student.query.all()
            allstudents = []
            for stu in students:
                student={"名字":stu.name,'性别' :stu.sex,'年龄':stu.age,'分数' :stu.score,'班级':stu.cls.name}
                allstudents.append(student)
            return allstudents



api.add_resource(getStudents,'/student/','/student/<stuid>')

