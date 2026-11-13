# Aula 12 - SQLite e o modelo

## Objetivos

- criar uma tabela SQLite;
- abrir e fechar uma conexão;
- separar consultas no arquivo `models.py`.

```python
import sqlite3
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db

def list_items():
    return get_db().execute(
        "SELECT * FROM items ORDER BY id DESC"
    ).fetchall()
```

Os `?` nas consultas recebem parâmetros separados. Isso é mais seguro do que
montar SQL concatenando texto enviado por um formulário.
