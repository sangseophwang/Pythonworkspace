# pymysql은 파이썬에서 mysql 연동을 도와주는 패키지입니다!! 아래와 같은 방식으로 mysql과 연결할 수 있습니다.


import pymysql
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

db = pymysql.connect(
    user='root',
    passwd='devpass',
    host='127.0.0.1',
    port=3306,
    db='elice_flask_board',
    charset='utf8'
)
cursor = db.cursor()


parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')


class Board(Resource):
    def get(self):
        sql = "SELECT id, name FROM `board`"
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify(status="success", result=result)

    def post(self):
        args = parser.parse_args()
        sql = "INSERT INTO `board` (`name`) VALUES (%s)"
        cursor.execute(sql, (args['name']))
        db.commit()

        return jsonify(status="success", result={"name": args["name"]})

    def put(self):
        args = parser.parse_args()
        sql = "UPDATE `board` SET name = %s WHERE `id` = %s"
        cursor.execute(sql, (args['name'], args["id"]))
        db.commit()

        return jsonify(status="success", result={"id": args["id"], "name": args["name"]})

    def delete(self):
        args = parser.parse_args()
        sql = "DELETE FROM `board` WHERE `id` = %s"
        cursor.execute(sql, (args["id"], ))
        db.commit()

        return jsonify(status="success", result={"id": args["id"]})


parser.add_argument('id')
parser.add_argument('title')
parser.add_argument('content')
parser.add_argument('board_id')


class BoardArticle(Resource):
    def get(self, board_id=None, board_article_id=None):
        if board_article_id:
            sql = "SELECT id, title, content FROM `boardArticle` WHERE `id`=%s"
            cursor.execute(sql, (board_article_id,))
            result = cursor.fetchone()
        else:
            sql = "SELECT id, title, content FROM `boardArticle` WHERE `board_id`=%s"
            cursor.execute(sql, (board_id,))
            result = cursor.fetchall()

        return jsonify(status="success", result=result)

    def post(self, board_id=None):
        args = parser.parse_args()
        sql = "INSERT INTO `boardArticle` (`title`, `content`, `board_id`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (args['title'], args['content'], args['board_id']))
        db.commit()

        return jsonify(status="success", result={"title": args["title"]})

    def put(self, board_id=None, board_article_id=None):
        args = parser.parse_args()
        sql = "UPDATE `boardArticle` SET title = %s, content = %s WHERE `id` = %s"
        cursor.execute(sql, (args['title'], args["content"], args["id"]))
        db.commit()

        return jsonify(status="success", result={"title": args["title"], "content": args["content"]})

    def delete(self, board_id=None, board_article_id=None):
        args = parser.parse_args()
        sql = "DELETE FROM `boardArticle` WHERE `id` = %s"
        cursor.execute(sql, (args["id"], ))
        db.commit()

        return jsonify(status="success", result={"id": args["id"]})


# API Resource 라우팅을 등록!
api.add_resource(Board, '/board')
api.add_resource(BoardArticle, '/board/<board_id>',
                 '/board/<board_id>/<board_article_id>')


if __name__ == '__main__':
    app.run(debug)
