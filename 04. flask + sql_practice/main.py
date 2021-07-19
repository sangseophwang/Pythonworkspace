from flask import Flask, jsonify, request, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base
from model.user_model import UserModel

engine = create_engine(
    "sqlite:///main.db",
    connect_args={"check_same_thread": False}
)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)


@app.route("/signup", methods=["POST"])
def signup():
    """회원가입"""
    # flask request 값 가져오기
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]

    user = session.query(UserModel).filter(
        UserModel.username == username).one_or_none()
    if user is not None:
        return Response("이미 존재하는 username입니다.", status=400)

    # sqlalchemy를 이용하여 db에 사용자 저장하기
    user = UserModel(username, password, name, email)
    session.add(user)
    session.commit()

    return Response("SUCCESS", status=201)


@app.route("/signin", methods=["POST"])
def signin():
    """로그인"""
    # flask request에서 값 가져오기
    username = request.json.get("username")
    password = request.json.get("password")

    # 값으로 db 조회하여 사용자 찾기
    user = session.query(UserModel).filter(
        UserModel.username == username,
        UserModel.password == password
    ).one_or_none()
    if user is None:
        return Response(status=204)

    return jsonify({
        "user_id": user.user_id,
        "username": user.username,
        "password": user.password,
        "name": user.name,
        "email": user.email
    })


@app.route("/user/password", methods=["PATCH"])
def change_password():
    username = request.json.get("username")
    password = request.json.get("password")

    new_password = request.json.get("new_password")

    if password == new_password:
        return Response("기존 비밀번호와 새로운 비밀번호는 동일할 수 없습니다.", status=400)

    user = session.query(
        UserModel
    ).filter(
        UserModel.username == username,
        UserModel.password == password
    ).one_or_none()
    if user is None:
        return Response(status=204)

    user.password = new_password
    session.add(user)
    session.commit()

    return Response("SUCCESS", status=200)


@app.route("/user", methods=["DELETE"])
def delete_user():
    username = request.json.get("username")
    password = request.json.get("password")

    user = session.query(
        UserModel
    ).filter(
        UserModel.username == username,
        UserModel.password == password
    ).one_or_none()
    if user is None:
        return Response(status=204)

    session.delete(user)
    session.commit()

    return Response("SUCCESS", status=200)


if __name__ == "__main__":
    app.run(debug=True)
