from sqlalchemy import Column, Integer, String, ForeignKey
from db.client import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    content = Column(String(), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, title=None, content=None, author_id=None, **entries):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.__dict__.update(entries)

    def get_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id
        }

    def __repr__(self):
        return f'<Article {self.title}>'
