from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base
from model.user_model import UserModel

engine = create_engine("sqlite:///main.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)


@app.route("/signup", methods=["POST"])
def signup():
    '''회원가입'''
    # flask request 값 가져오기
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    email = request.form.get("email")

    # sqlalchemy를 이용해 db에 사용자 저장하기
    user = UserModel(username, password, name, email)
    session.add(user)
    session.commit()

    return "SUCCESS"


@app.route("/signin", methods=["POST"])
def signin():
    '''로그인'''
    # flask request에서 값 가져오기
    username = request.form.get("username")
    password = request.form.get("password")

    # 값으로 db 조회하여 사용자 찾기
    user = session.query(UserModel).filter(
        UserModel.username == username, UserModel.password == password).one_or_none()
    if user is None:
        return "No User"

    return jsonify({
        "user_id": user.user_id,
        "username": user.username,
        "password": user.password,
        "name": user.name,
        "email": user.email
    })


app.run(debug=True)

# def change_password():
#     '''비밀번호 변경'''
#     pass


# def delete_user():
#     '''삭제'''
#     pass
