import datetime
import os

import jwt
import sqlalchemy.exc

from app import SWAGGER_DIR
from flasgger import Swagger, swag_from
from db.client import db_session
from app import app
from flask import request, jsonify, make_response
from db.models.user import User

base_headers = {"Content-Type": "application/json"}


@app.route("/api/v1/user/registration", methods=["POST"])
@swag_from(os.path.join(SWAGGER_DIR, "registration.yml"))
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
@swag_from(os.path.join(SWAGGER_DIR, "session.yml"))
def session():
    user = request.get_json()
    return authorization(user["email"], user["password"])


def authorization(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    if user is not None:
        return generate_token(user)
    else:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


def generate_token(user):
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=30)
    }, app.config["SECRET_KEY"])
    return jsonify({'token': token.decode("utf-8")})
