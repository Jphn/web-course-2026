# Solução 13 - Criar e listar

`app/models.py`:

```python
# app/models.py
def list_items():
    return get_db().execute(
        "SELECT * FROM items ORDER BY created_at DESC, id DESC"
    ).fetchall()


def create_item(name, category, description):
    db = get_db()
    db.execute(
        "INSERT INTO items (name, category, description) VALUES (?, ?, ?)",
        (name, category, description),
    )
    db.commit()
```

`app/routes.py`:

```python
# app/routes.py
def register_routes(app):
    @app.route("/items/")
    def items():
        return render_template("items/list.html", items=list_items())
```
