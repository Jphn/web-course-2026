# Solução 10 - Formulário de contato

```python
# app/routes.py
from flask import redirect, render_template, request, url_for

def register_routes(app):
    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            message = request.form.get("message", "").strip()
            return redirect(url_for("contact", name=name, message=message))

        return render_template(
            "contact.html",
            name=request.args.get("name", ""),
            message=request.args.get("message", ""),
        )
```

`templates/contact.html`:

```html
<!-- templates/contact.html -->
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Contato</title>
</head>
<body>
    <h1>Entre em contato</h1>

    <form method="post">
        <label for="name">Nome</label>
        <input type="text" id="name" name="name" value="{{ name }}">

        <label for="message">Mensagem</label>
        <textarea id="message" name="message">{{ message }}</textarea>

        <button type="submit">Enviar</button>
    </form>

    {% if message %}
        <p>Obrigado, {{ name }}. Recebemos sua mensagem:</p>
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
```
