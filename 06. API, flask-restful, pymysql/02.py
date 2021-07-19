# Flask-restful 실습
# 실습의 코드를 통해 flask-restful 패키지의 사용법을 알아봅시다!

# reqparse
# 클라이언트로부터 전달받은 데이터를 쉽게 접근할 수 있는 모듈입니다.

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# 임시 데이터베이스!
DB = {
    "1": {"msg": "Hello"},
    "2": {"msg": "Elice!"}
}

# parser 변수를 통해 클라이언트로부터 전달 받는 인자들을 지정할 수 있습니다.
parser = reqparse.RequestParser()
parser.add_argument("id")
parser.add_argument("msg")


class Board(Resource):
    def get(self):
        # DB에 있는 정보를 전부 다 json 형태로 반환
        return jsonify(status="success", result=DB)

    def post(self):
        # 클라이언트로부터 전달 받은 정보, id와 msg를 가지고 있다
        args = parser.parse_args()
        # DB에 정보 추가

        if args['id'] in DB:
            return jsonify(status="fail", message="id가 이미 있습니다.")
        DB[args["id"]] = {'msg': args['msg']}

        return jsonify(status="success", result=DB[args["id"]])

    def put(self):
        # 클라이언트로부터 전달 받은 정보, id와 msg를 가지고 있다
        args = parser.parse_args()
        # DB에서 정보 수정

        if not args['id'] in DB:
            return jsonify(status='fali', message="해당 id가 없습니다.")

        DB[args["id"]] = {'msg': args['msg']}

        return jsonify(status="success", result=DB[args["id"]])

    def delete(self):
        # 클라이언트로부터 전달 받은 정보, id와 msg를 가지고 있다
        args = parser.parse_args()
        # DB에서 정보 삭제

        if not args['id'] in DB:
            return jsonify(status="fail", message='해당 id가 없습니다.')

        DB.pop(args['id'])

        return jsonify(status="success", result=args["id"])


# API Resource 라우팅을 등록!
api.add_resource(Board, '/board')


if __name__ == '__main__':
    app.run()
