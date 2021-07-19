# 1. 전체 코드를 읽어보고 flask_restful 패키지의 사용법을 확인해보세요!
# 2. msg 변수에 dictionary type으로 환영 메세지를 입력해보세요!

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloElice(Resource):
    def get(self):
        # msg 변수에 dictionary type으로 메세지를 입력해보세요!!
        msg = {
            'message': 'Hello Elice!'
        }
        return jsonify(status="success", result=msg)

    def post(self):
        pass


api.add_resource(HelloElice, '/')

if __name__ == '__main__':
    app.run()
