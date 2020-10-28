import os
from flasgger import Swagger
from flask import Flask

swagger_template = {
    'securityDefinitions': {
        "Token": {
            "name": "Authorization",
            "type": "apiKey",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "in": "header",
        }
    }
}
app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Load mock service API 0.1',
    'description': "Данный сервис предназначен для проведения пробных нагрузочных тестов.",
    'uiversion': 3
}

DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

app.config["SECRET_KEY"] = "thisismysecretkey"
app.config["DATABASE_URL"] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
swagger = Swagger(app, template=swagger_template)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SWAGGER_DIR = os.path.join(BASE_DIR, "swagger")
