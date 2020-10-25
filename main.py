from app import app

import api.routes_article
import api.routes_user

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
