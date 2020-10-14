from flask import Flask, request, Response
from clients.db_client import DbClient


app = Flask(__name__)


@app.route("/api/v1/user/<user_uid>/article", methods=["GET"])
def get_article():
    pass


@app.route("/api/v1/article", methods=["POST"])
def add_article():
    request.get_json()


@app.route("/api/v1/user/<user_uid>/article/<uid>", methods=["PATCH"])
def upd_article():
    request.get_json()


@app.route("/api/v1/user/<user_uid>/article/<uid>", methods=["GET"])
def get_article_by_uid(uid):
    pass


@app.route("/api/v1/user/<user_uid>/article/<uid>", methods=["DELETE"])
def del_article_by_uid(uid):
    pass


@app.route("api/v1/registration", methods=["POST"])
def registration():
    pass


@app.route("api/v1/session", methods=["POST"])
def authorization():
    pass







