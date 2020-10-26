import os

from flasgger import Swagger
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)

app.config["SECRET_KEY"] = "thisismysecretkey"
app.config["DATABASE_URL"] = 'postgresql://admin:admin@127.0.0.1/lock_service'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SWAGGER_DIR = os.path.join(BASE_DIR, "swagger")
