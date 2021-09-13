from sqlalchemy import Column, Integer, String
from db import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=20))
    email = Column(String(length=50))
    password = Column(String(length=200))
