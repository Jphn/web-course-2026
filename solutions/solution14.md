# Solução 14 - CRUD completo

`app/models.py`:

```python
# app/models.py
def get_item(id):
    return get_db().execute(
        "SELECT * FROM items WHERE id = ?", (id,)
    ).fetchone()


def update_item(id, name, category, description):
    db = get_db()
    db.execute(
        """
        UPDATE items
        SET name = ?, category = ?, description = ?
        WHERE id = ?
        """,
        (name, category, description, id),
    )
    db.commit()


def delete_item(id):
    db = get_db()
    db.execute("DELETE FROM items WHERE id = ?", (id,))
    db.commit()
```

As rotas carregam o registro pelo `id`, exibem o formulário no GET e salvam a
alteração no POST. A exclusão aceita somente POST e redireciona para a lista.
