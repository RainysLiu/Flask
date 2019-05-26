
from flask_restful import Api

from tppapp.models import Letter, City

api = Api()



from flask import request
from flask_restful import Api, Resource, marshal_with, fields, marshal



city_fields = {
    "id":fields.Integer,
    "regionName":fields.String,
    "cityCode":fields.Integer,
    "pinYin":fields.String,
}

letter_fields = {
    "A":fields.List(fields.Nested(city_fields)),
    "B":fields.List(fields.Nested(city_fields)),
    "C":fields.List(fields.Nested(city_fields)),
    "D":fields.List(fields.Nested(city_fields)),
    "E":fields.List(fields.Nested(city_fields)),
    "F":fields.List(fields.Nested(city_fields)),
    "G":fields.List(fields.Nested(city_fields)),
    "H":fields.List(fields.Nested(city_fields)),
    "J":fields.List(fields.Nested(city_fields)),
    "K":fields.List(fields.Nested(city_fields)),
    "L":fields.List(fields.Nested(city_fields)),
    "M":fields.List(fields.Nested(city_fields)),
    "N":fields.List(fields.Nested(city_fields)),
    "P":fields.List(fields.Nested(city_fields)),
    "Q":fields.List(fields.Nested(city_fields)),
    "R":fields.List(fields.Nested(city_fields)),
    "S":fields.List(fields.Nested(city_fields)),
    "T":fields.List(fields.Nested(city_fields)),
    "W":fields.List(fields.Nested(city_fields)),
    "X":fields.List(fields.Nested(city_fields)),
    "Y":fields.List(fields.Nested(city_fields)),
    "Z":fields.List(fields.Nested(city_fields)),
}

simple_city_fields = {
    'returnCode':fields.String,
    'returnValue':fields.Nested(letter_fields)
}

class SimpleCityResource(Resource):
    @marshal_with(simple_city_fields)
    def get(self):
        return_value = {}
        letters = Letter.query.all() # 查询所有的字母
        for l in letters:  # 遍历每个字母
            cities = City.query.filter_by(letter_id=l.id) # 查询当前正在遍历的字母对应的多个城市
            return_value[l.letter] = cities

        return {"returnCode":"0","returnValue":return_value}


class CleverCityResource(Resource):

    def get(self):

        dynamic_letter_fields = {}   # 存储动态生成的字母与它关联的城市

        return_value = {}
        letters = Letter.query.all()  # 查询所有的字母
        for l in letters:  # 遍历每个字母
            cities = City.query.filter_by(letter_id=l.id)  # 查询当前正在遍历的字母对应的多个城市
            return_value[l.letter] = cities

            dynamic_letter_fields[l.letter] = fields.List(fields.Nested(city_fields))

        # 最终的响应定制输出格式（格式化输出）
        result_fields = {"returnCode": fields.String,"returnValue":fields.Nested(dynamic_letter_fields)}

        data = {"returnCode":"0","returnValue":return_value}

        return marshal(data,result_fields)


class ArgsResource(Resource):

    def get(self):
        data = {}

        username = request.args.get("username")  # 接收Get请求参数
        if username is None:
            data["msg"] = "您没有输入username参数"
        else:
            data["msg"] = "你好，" + username
        return {"info":data}


api.add_resource(SimpleCityResource,'/simple/')
api.add_resource(CleverCityResource,'/clever/')
api.add_resource(ArgsResource,'/args/')



