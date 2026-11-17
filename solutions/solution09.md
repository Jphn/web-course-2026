# Solução 9 - Navegação

`app/routes.py`:

```python
# app/routes.py
def register_routes(app):
    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")
```

`app/templates/base.html`:

```html
<!-- app/templates/base.html -->
<a href="{{ url_for('about') }}">Sobre</a>
<a href="{{ url_for('contact') }}">Contato</a>
```

`app/templates/items/list.html` é o primeiro template da lista e pode exibir
uma mensagem de que ainda não há itens cadastrados.
