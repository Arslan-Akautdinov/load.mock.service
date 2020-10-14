from typing import List
from models.article import Article


class DbClient:

    def __init__(self):
        pass

    # ARTICLES

    def create_article(self, article: Article) -> Article:
        pass

    def select_article(self) -> List[Article]:
        pass

    def select_article_by_uid(self, uid) -> Article:
        pass

    def delete_article_by_uid(self, uid):
        pass

    # USERS

    def create_user(self, email, password):
        pass

    def delete_user(self, uid):
        pass



