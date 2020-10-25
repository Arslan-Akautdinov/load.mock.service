from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisismysecretkey"
app.config["DATABASE_URL"] = 'postgresql://admin:admin@127.0.0.1/lock_service'







