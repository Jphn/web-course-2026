# app/__init__.py - Application Factory (Production Ready)
import os
import logging
from flask import Flask, render_template, request
from dotenv import load_dotenv
from .models import init_db, close_db

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

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

    # Template filter
    from datetime import datetime
    @app.template_filter('days_ago')
    def days_ago_filter(date_str):
        try:
            date = datetime.strptime(date_str[:10], '%Y-%m-%d').date()
            return (datetime.now().date() - date).days
        except:
            return '-'

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        logger.warning(f'404: {request.url}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        logger.error(f'500: {e}', exc_info=True)
        return render_template('errors/500.html'), 500

    return app