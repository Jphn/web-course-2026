# app/__init__.py - Application Factory
import os
from flask import Flask
from .models import init_db, close_db

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    from .routes.main import main_bp
    from .routes.items import items_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp)

    return app