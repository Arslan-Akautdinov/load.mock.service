from sqlalchemy import Column, String, Integer
from db.client_base import DBClientBase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(150))
    password = Column(String(150))


class DBClientUser(DBClientBase):

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()


Base.metadata.create_all()
