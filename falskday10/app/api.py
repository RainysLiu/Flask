from flask_restful import Resource, Api


api = Api()





class Test(Resource):
    def get(self):
        return {'info':'这是在测试！'}



api.add_resource(Test,'/')





