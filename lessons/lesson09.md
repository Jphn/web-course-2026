# Aula 9 - Rotas e navegação

## Pré-requisito

Use a aplicação Flask criada na Aula 8 e os templates organizados nas aulas
anteriores.

## Objetivos

- criar mais de uma rota;
- renderizar templates;
- gerar links com `url_for`.

```python
# app/routes.py
from flask import render_template

def register_routes(app):
    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")
```

No template, prefira:

```html
<!-- app/templates/base.html -->
<a href="{{ url_for('about') }}">Sobre</a>
```

Assim o caminho fica definido em um só lugar. Nesta aula, a turma conecta as
páginas inicial, sobre, contato e uma primeira página de itens:

```python
# app/routes.py
def register_routes(app):
    @app.route("/items/")
    def items():
        return render_template("items/list.html", items=[])
```

No `create_app()`, registre as rotas uma vez:

```python
# app/__init__.py
from .routes import register_routes

register_routes(app)
```

As funções de rota das próximas aulas também serão adicionadas à mesma
função `register_routes(app)`.

Crie o template inicial da lista:

```html
<!-- app/templates/items/list.html -->
{% extends "base.html" %}

{% block title %}Itens{% endblock %}

{% block content %}
<h1>Itens</h1>
<p>Nenhum item cadastrado.</p>
{% endblock %}
```

Neste momento a lista ainda está vazia; o banco de dados será ligado a ela
mais adiante.

## Exercício (10 min)

Adicione as páginas `/about` e `/contact`, usando templates que estendem
`base.html`. Atualize a navegação com links gerados por `url_for()`.

## Checklist

- [ ] As rotas `/about` e `/contact` funcionam
- [ ] As páginas usam `render_template()`
- [ ] Os links usam `url_for()`
- [ ] A rota `/items/` mostra `items/list.html`
- [ ] O template da lista estende `base.html`
