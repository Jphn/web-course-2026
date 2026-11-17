# Aula 14 - Editar e excluir

## Pré-requisito

A aplicação já permite criar e listar itens. Nesta aula, vamos completar o
CRUD com edição e exclusão.

## Objetivos

- carregar um item pelo seu `id`;
- reaproveitar o formulário para edição;
- atualizar um registro;
- excluir usando uma requisição POST.

## Funções do modelo

Em `app/models.py`, busque um item pelo identificador:

```python
# app/models.py
def get_item(id):
    return get_db().execute(
        "SELECT * FROM items WHERE id = ?", (id,)
    ).fetchone()
```

Atualize somente o registro correspondente:

```python
# app/models.py
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
```

A exclusão também usa um parâmetro e precisa de `commit()`:

```python
# app/models.py
def delete_item(id):
    db = get_db()
    db.execute("DELETE FROM items WHERE id = ?", (id,))
    db.commit()
```

## Rotas

Uma rota de edição combina GET e POST:

```python
# app/routes.py
def register_routes(app):
    @app.route("/items/<int:id>/edit", methods=["GET", "POST"])
    def edit_item(id):
        item = get_item(id)
        if item is None:
            return "Item não encontrado", 404

        if request.method == "POST":
            name = request.form.get("name", "").strip()
            category = request.form.get("category", "").strip()
            description = request.form.get("description", "").strip()
            update_item(id, name, category, description)
            flash("Item atualizado com sucesso!", "success")
            return redirect(url_for("items"))

        return render_template(
            "items/form.html",
            title="Editar item",
            name=item["name"],
            category=item["category"],
            description=item["description"],
            item=item,
        )
```

A exclusão usa um formulário próprio com POST:

```python
# app/routes.py
def register_routes(app):
    @app.post("/items/<int:id>/delete")
    def delete_item_route(id):
        if get_item(id) is None:
            return "Item não encontrado", 404
        delete_item(id)
        return redirect(url_for("items"))
```

No template da lista, os botões podem ser:

```html
<!-- app/templates/items/list.html -->
<div class="form-actions">
    <a href="{{ url_for('edit_item', id=item.id) }}"
       class="btn btn-secondary">Editar</a>
    <form method="post"
          action="{{ url_for('delete_item_route', id=item.id) }}">
        <button type="submit" class="btn btn-danger">Excluir</button>
    </form>
</div>
```

O botão de exclusão fica dentro de um formulário próprio porque excluir altera
dados. Reutilize a validação da Aula 11 antes de chamar `update_item()`. A
confirmação no navegador pode ser adicionada como melhoria.

No formulário de edição, mostre também um botão de exclusão quando `item`
estiver disponível:

```html
<!-- app/templates/items/form.html -->
{% if item %}
<form method="post" action="{{ url_for('delete_item_route', id=item.id) }}">
    <button type="submit" class="btn btn-danger">Excluir item</button>
</form>
{% endif %}
```

## Exercício (10 min)

Adicione edição e exclusão à lista de itens. Teste também o comportamento para
um `id` que não existe.

## Checklist

- [ ] `get_item()` busca pelo `id`
- [ ] o formulário é reutilizado para edição
- [ ] `update_item()` usa `WHERE id = ?`
- [ ] `delete_item()` usa POST e chama `commit()`
- [ ] itens inexistentes retornam 404
- [ ] editar e excluir atualizam a lista
