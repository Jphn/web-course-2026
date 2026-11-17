# Aula 12 - SQLite e o modelo

## Pré-requisito

Agora a aplicação já possui a fábrica criada nas aulas anteriores. Configure
onde o banco será salvo dentro de `create_app()`:

```python
# app/__init__.py
import os

app.config["DATABASE"] = os.path.join(app.root_path, "app.db")
```

Coloque essa configuração depois de criar `app`, antes de chamar qualquer
função que use o banco.

## Objetivos

- criar uma tabela SQLite;
- abrir e fechar uma conexão;
- separar consultas no arquivo `models.py`.

## Conexão com o banco

Crie `app/models.py`. A conexão fica guardada em `g` para ser reutilizada
durante uma requisição:

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
```

`current_app` representa a aplicação Flask em execução. `sqlite3.Row` permite
acessar as colunas pelo nome, como `item["name"]`.

## Criando a tabela

No mesmo arquivo, crie a tabela apenas se ela ainda não existir:

```python
# app/models.py
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

Ainda não vamos inserir ou listar itens. Essas operações serão criadas na
Aula 13.

## Ligando o modelo à aplicação

Em `app/__init__.py`, importe as funções e configure o banco dentro de
`create_app()`:

```python
# app/__init__.py
from .models import close_db, init_db

app.config["DATABASE"] = os.path.join(app.root_path, "app.db")

with app.app_context():
    init_db()

app.teardown_appcontext(close_db)
```

`app.app_context()` permite que `init_db()` use `current_app` durante a
inicialização. `teardown_appcontext()` fecha a conexão ao fim de cada
requisição.

## Exercício (10 min)

Crie `app/models.py`, configure o caminho do banco e conecte o modelo à
aplicação. Depois, inicie o servidor e confirme que o arquivo `app.db` e a
tabela `items` foram criados.

## Checklist

- [ ] `DATABASE` aponta para `app/app.db`
- [ ] `get_db()` reutiliza a conexão guardada em `g`
- [ ] `close_db()` fecha a conexão
- [ ] `init_db()` cria a tabela `items`
- [ ] `init_db()` é chamado dentro de um contexto da aplicação
- [ ] o arquivo do banco é criado ao iniciar a aplicação
