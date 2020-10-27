import os

from flasgger import Swagger
from flask import Flask

swagger_template = {
    'securityDefinitions': {
        "BearerAuth": {
            "name": "authorization",
            "type": "apiKey",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "in": "header",
        }
    }
}
app = Flask(__name__)
swagger = Swagger(app, template=swagger_template)

app.config["SECRET_KEY"] = "thisismysecretkey"
app.config["DATABASE_URL"] = 'postgresql://admin:admin@127.0.0.1/lock_service'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SWAGGER_DIR = os.path.join(BASE_DIR, "swagger")
