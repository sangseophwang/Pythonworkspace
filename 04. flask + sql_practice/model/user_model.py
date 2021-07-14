from sqlalchemy import Column, String, Integer, Sequence
from model import Base


class UserModel(Base):
    __tablename__ = "user"
    # user_id 에 sequence를 넣어서 넣을 때마다 1씩 증가하도록 설정함.
    user_id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    name = Column(String(15))
    email = Column(String(320))

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
