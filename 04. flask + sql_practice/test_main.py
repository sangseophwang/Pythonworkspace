import unittest
from main import app, session
from model.user_model import UserModel


class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        test_user = session.query(UserModel).filter(
            UserModel.username == "test_user"
        ).delete()
        session.commit()

    def test_success_signup(self):
        response = self.test_app.post(
            "/signup",
            json={
                "username": "test_user",
                "password": "pw2",
                "name": "name2",
                "email": "2@naver.com"
            }
        )
        self.assertEqual(201, response.status_code)

        user = session.query(UserModel).filter(
            UserModel.username == "test_user",
            UserModel.password == "pw2",
            UserModel.name == "name2",
            UserModel.email == "2@naver.com"
        ).one_or_none()
        self.assertIsNotNone(user)

    def test_exist_username(self):
        user = UserModel("test_user", "pw", "name", "email@email.com")
        session.add(user)
        session.commit()

        response = self.test_app.post(
            "/signup",
            json={
                "username": "test_user",
                "password": "pw2",
                "name": "name2",
                "email": "2@naver.com"
            }
        )
        self.assertEqual(400, response.status_code)


class TestSignIn(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()
        user = UserModel("test_user", "pw", "john", "email@email.com")
        session.add(user)
        session.commit()

    def tearDown(self):
        session.query(UserModel).filter(
            UserModel.username == "test_user").delete()
        session.commit()

    def test_success_signin(self):
        response = self.test_app.post(
            "/signin",
            json={
                "username": "test_user",
                "password": "pw"
            }
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json.get("name"), "john")
        self.assertEqual(response.json.get("email"), "email@email.com")

    def test_no_user(self):
        response = self.test_app.post(
            "/signin",
            json={
                "username": "gjdklsgajlkdsajfdlsjfkdsl",
                "password": "h4qhwirhowiqrhdvncmx34"
            }
        )
        self.assertEqual(204, response.status_code)


unittest.main()


'''
POST /signup
json body data

response
response의 status, message를 확인한다!

'''
