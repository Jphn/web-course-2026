# Aula 8 - Primeiro aplicativo Flask

## Objetivos

- instalar Flask em um ambiente virtual;
- criar a aplicação e iniciar o servidor;
- entender a relação entre Python, rota e navegador.

## Código inicial

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Olá, Flask!"

    return app
```

```python
# run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

`debug=True` ajuda durante a aula e não deve ser usado como configuração de
produção.
