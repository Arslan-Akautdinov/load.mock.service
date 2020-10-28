import jwt
import sqlalchemy.exc
import json
import os

from app import SWAGGER_DIR
from app import app
from flask import request, jsonify, make_response
from flasgger import swag_from
from db.client import db_session
from db.models.article import Article


def check_for_token(headers):
    if "Authorization" not in headers:
        return jsonify({"error": "Missing token"}), 403
    try:
        token = headers["Authorization"]
        decoded = jwt.decode(token, app.config["SECRET_KEY"])
        return {"user_id": decoded["user_id"]}
    except Exception as ex:
        return jsonify({"error": "Invalid token"}), 403


@app.route("/api/v1/article", methods=["GET"])
@swag_from(os.path.join(SWAGGER_DIR, "get_article.yml"))
def get_article():
    try:
        selected_articles = Article.query.filter_by().all()
        if selected_articles is not None:
            return make_response(json.dumps([article.get_dict() for article in selected_articles]), 200, {"Content-Type": "application/json"})
        else:
            return make_response([], 200, {"Content-Type": "application/json"})
    except sqlalchemy.exc.IntegrityError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)


@app.route("/api/v1/article/author", methods=["GET"])
@swag_from(os.path.join(SWAGGER_DIR, "get_article_user.yml"))
def get_article_author():
    try:
        if "user_id" in check_for_token(request.headers):
            user_id = check_for_token(request.headers)["user_id"]
        else:
            return check_for_token(request.headers)
        selected_articles: list = Article.query.filter_by(Article.author_id == user_id).all()
        if len(selected_articles) != 0:
            return make_response(json.dumps([article.get_dict() for article in selected_articles]), 200, {"Content-Type": "application/json"})
        else:
            return make_response([], 200, {"Content-Type": "application/json"})
    except sqlalchemy.exc.IntegrityError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)


@app.route("/api/v1/article", methods=["POST"])
@swag_from(os.path.join(SWAGGER_DIR, "add_article.yml"))
def add_article():
    try:
        if "user_id" in check_for_token(request.headers): user_id = check_for_token(request.headers)["user_id"]
        else: return check_for_token(request.headers)
        created_article = Article(**request.get_json())
        created_article.author_id = user_id
        db_session.add(created_article)
        db_session.commit()
        db_session.refresh(created_article)
        return make_response(jsonify(created_article.get_dict()), 201)
    except sqlalchemy.exc.SQLAlchemyError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)


@app.route("/api/v1/article/<article_id>", methods=["GET"])
@swag_from(os.path.join(SWAGGER_DIR, "get_article_by_id.yml"))
def get_article_by_id(article_id: int):
    try:
        selected_article: Article = Article.query.filter_by(id=article_id).first()
        if selected_article is not None:
            return make_response(json.dumps(selected_article.get_dict()), 200, {"Content-Type": "application/json"})
        else:
            return make_response(jsonify({"errors": "not found."}), 404, {"Content-Type": "application/json"})
    except sqlalchemy.exc.SQLAlchemyError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)


@app.route("/api/v1/article/author/<article_id>", methods=["GET"])
@swag_from(os.path.join(SWAGGER_DIR, "get_article_user_by_id.yml"))
def get_article_author_by_id(article_id: int):
    try:
        if "user_id" in check_for_token(request.headers):
            user_id = check_for_token(request.headers)["user_id"]
        else:
            return check_for_token(request.headers)
        selected_article: Article = Article.query.filter(Article.id == article_id, Article.author_id == user_id).first()
        if selected_article is not None:
            return make_response(json.dumps(selected_article.get_dict()), 200, {"Content-Type": "application/json"})
        else:
            return make_response(jsonify({"errors": "not found."}), 404, {"Content-Type": "application/json"})
    except sqlalchemy.exc.SQLAlchemyError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)


@app.route("/api/v1/article/<article_id>", methods=["DELETE"])
@swag_from(os.path.join(SWAGGER_DIR, "del_article.yml"))
def del_article_by_id(article_id: int):
    try:
        if "user_id" in check_for_token(request.headers):
            user_id = check_for_token(request.headers)["user_id"]
        else:
            return check_for_token(request.headers)
        result = Article.query.filter(Article.id == article_id, Article.author_id == user_id).first()
        if result is not None:
            Article.query.filter(Article.id == article_id, Article.author_id == user_id).delete()
            db_session.commit()
        else:
            return make_response(jsonify({"errors": "not found"}), 404)
        return make_response({"message": "ok"}, 200)
    except sqlalchemy.exc.SQLAlchemyError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)
