# Solução 8 - Primeira rota Flask

`app/__init__.py`:

```python
# app/__init__.py
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Olá, Flask!"

    @app.route("/hello")
    def hello():
        return """
        <h1>Olá, estudante!</h1>
        <p>Esta é minha primeira rota Flask.</p>
        """

    return app
```

`run.py`:

```python
# run.py
from app import create_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
```
