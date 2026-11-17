# Solução 12 - Banco de dados

`app/__init__.py`:

```python
# app/__init__.py
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
```

`app/models.py`:

```python
# app/models.py
import sqlite3

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(current_app.config["DATABASE"]) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        db.commit()
```
