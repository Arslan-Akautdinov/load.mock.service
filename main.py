import os
from app import app

import api.routes_article
import api.routes_user

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("APP_PORT"), debug=True)
