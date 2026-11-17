# Solução 11 - Validação

`app/routes.py`:

```python
# app/routes.py
name = request.form.get("name", "").strip()
category = request.form.get("category", "").strip()
description = request.form.get("description", "").strip()

if not name or not category:
    flash("Preencha o nome e a categoria.", "error")
    return render_template(
        "items/form.html",
        title="Novo item",
        name=name,
        category=category,
        description=description,
    ), 400

if category not in ("work", "personal", "study"):
    flash("Escolha uma categoria válida.", "error")
    return render_template(
        "items/form.html",
        title="Novo item",
        name=name,
        category=category,
        description=description,
    ), 400
```

A rota lê os campos com `request.form.get()`, verifica os valores permitidos,
usa `flash()` para informar o erro e retorna o mesmo template com os valores
preenchidos.
