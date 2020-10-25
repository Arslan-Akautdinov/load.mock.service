from db.client_article import DBClientArticle, Article
from flask import Response, request
from app import app

db_article = DBClientArticle()
base_headers = {"Content-Type": "application/json"}


@app.route("/api/v1/article", methods=["GET"])
def get_article():
    return Response(db_article.select_article(), status=200, headers=base_headers)


@app.route("/api/v1/article", methods=["POST"])
def add_article():
    request.get_json()
    article = Article()
    return Response(db_article.create_article(article), status=201, headers=base_headers)


@app.route("/api/v1/article/<article_id>", methods=["GET"])
def get_article_by_id(article_id):
    return Response(db_article.select_article(article_id), status=200, headers=base_headers)


@app.route("/api/v1/article/<article_id>", methods=["DELETE"])
def del_article_by_id(article_id):
    return Response(db_article.create_article(article_id), status=200, headers=base_headers)
