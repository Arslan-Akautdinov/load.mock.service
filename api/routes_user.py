import datetime
import jwt
from app import app
from flask import request, jsonify, make_response
from db.client_user import DBClientUser


db_article = DBClientUser()
base_headers = {"Content-Type": "application/json"}


@app.route("/api/v1/registration", methods=["POST"])
def registration():
    pass


@app.route("/api/v1/login", methods=["POST"])
def login():
    auth = request.get_json()
    if auth and auth['password'] == 'password':
        token = jwt.encode({
            'user': 'test',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=30)
        }, app.config["SECRET_KEY"])
        return jsonify({'token': token.decode("utf-8")})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})