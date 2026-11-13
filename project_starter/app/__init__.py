import os

from flask import Flask

from .models import close_db, init_db


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret"
    app.config["DATABASE"] = os.path.join(app.root_path, "app.db")

    with app.app_context():
        init_db()
    app.teardown_appcontext(close_db)

    from .routes import register_routes

    register_routes(app)
    return app