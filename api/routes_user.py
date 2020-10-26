import datetime
import jwt
import sqlalchemy.exc

from flasgger import Swagger
from db.client import db_session
from app import app
from flask import request, jsonify, make_response
from db.models.user import User

base_headers = {"Content-Type": "application/json"}


@app.route("/api/v1/user/registration", methods=["POST"])
def registration():
    try:
        req = request.get_json()
        user: User = User(req["email"], req["password"])
        db_session.add(user)
        db_session.commit()
        return make_response(jsonify({"message": "ok"}), 201)
    except sqlalchemy.exc.SQLAlchemyError as e:
        return make_response(jsonify({"errors": e.args}), 422)
    except Exception as e:
        return make_response(jsonify({"errors": e}), 500)


@app.route("/api/v1/user/session", methods=["POST"])
def session():
    auth = request.get_json()
    if auth and auth['password'] == 'password':
        token = jwt.encode({
            'user': 'test',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=30)
        }, app.config["SECRET_KEY"])
        return jsonify({'token': token.decode("utf-8")})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})