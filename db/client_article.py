from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db.client_base import DBClientBase

Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    content = Column(String())
    author_id = Column(Integer, ForeignKey('users.id'))


class DBClientArticle(DBClientBase):

    def __init__(self):
        pass

    def create_article(self, article: Article):
        self.session.add(article)
        self.session.commit()

    def select_article(self, article_id=None):
        if article_id:
            return self.session.query(Article).filter(Article.id == article_id)
        else:
            return self.session.query(Article)


Base.metadata.create_all()
