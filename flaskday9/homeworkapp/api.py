import os

from flask_restful import Resource, Api, fields, marshal_with
import json

api = Api()






class getJieQi(Resource):
    def get(self):
        with open(os.path.join('E:\工作区\FaskWork\\flaskday9\homeworkapp\\resource\jieqi.json'), 'rb') as f:
            info = json.load(f)
        data = info['data']
        jieqi =data['jieqi']
        return {'eight':jieqi['8'],'23rd':jieqi['23']}




api.add_resource(getJieQi,'/jieqi')




