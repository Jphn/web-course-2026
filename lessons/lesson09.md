# Aula 9 - Rotas e Métodos HTTP

## Objetivos

- Entender GET vs POST
- Lidar com ambos métodos em uma rota
- Usar redirect e url_for para padrão PRG

## Conteúdo (30 min)

1. **Métodos HTTP**:
    - GET: buscar dados (seguro, cacheável, bookmarkável)
    - POST: enviar dados (altera estado, não cacheável)
2. **Rota com Métodos no Flask**: `@app.route('/path', methods=['GET', 'POST'])`
3. **Objeto Request**: `request.method` retorna `'GET'` ou `'POST'`
4. **Redirect**: `return redirect(url_for('endpoint'))`
5. **Padrão PRG**: POST → processa → redirect para GET → previne duplicação no refresh

## Prática Guiada (40 min) - Code Along

```python
# app/routes/items.py
from flask import Blueprint, render_template, request, redirect, url_for

items_bp = Blueprint('items', __name__, url_prefix='/items')

# Lista em memória por enquanto (banco nas próximas aulas)
ITEMS = []

@items_bp.route('/', methods=['GET', 'POST'])
def list_items():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            ITEMS.append({'id': len(ITEMS) + 1, 'name': name})
        return redirect(url_for('items.list_items'))

    return render_template('items/list.html', items=ITEMS)
```

```html
<!-- templates/items/list.html -->
{% extends 'base.html' %} {% from 'macros.html' import render_field %} {% block
title %}Itens{% endblock %} {% block content %}
<div class="page-header">
	<h1>Itens</h1>
</div>

<form method="POST" class="form">
	{{ render_field('name', 'Nome do Item', 'text', '', true) }}
	<button type="submit" class="btn btn-primary">Adicionar</button>
</form>

{% if items %}
<table class="table">
	<thead>
		<tr>
			<th>ID</th>
			<th>Nome</th>
		</tr>
	</thead>
	<tbody>
		{% for item in items %}
		<tr>
			<td>{{ item.id }}</td>
			<td>{{ item.name }}</td>
		</tr>
		{% endfor %}
	</tbody>
</table>
{% else %}
<p>Nenhum item ainda.</p>
{% endif %} {% endblock %}
```

```python
# app/__init__.py (atualizar)
def create_app():
    app = Flask(__name__)
    app.secret_key = 'dev-secret-change-in-production'

    from .routes.main import main_bp
    from .routes.items import items_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp)

    return app
```

```css
/* Adicionar ao static/css/style.css */
.page-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 1.5rem;
	flex-wrap: wrap;
	gap: 1rem;
}
.table {
	width: 100%;
	border-collapse: collapse;
	background: white;
	border-radius: var(--radius);
	overflow: hidden;
	box-shadow: var(--shadow);
}
.table th,
.table td {
	padding: 1rem;
	text-align: left;
	border-bottom: 1px solid #eee;
}
.table th {
	background: var(--primary);
	color: white;
}
```

## Exercício (10 min)

Criar rota `/greet/<name>` no `main.py`:

- GET: renderiza template mostrando "Hello, {name}!"
- POST: redirect para mesma rota (padrão PRG)
- Testar com formulário que POSTa para mesma URL

---

## Checklist

- [ ] Blueprint `items` com `url_prefix='/items'`
- [ ] Rota lida GET (listar) e POST (criar)
- [ ] Padrão PRG: redirect após POST
- [ ] Formulário submete para mesma URL
- [ ] `url_for('items.list_items')` funciona
- [ ] Exercício: `/greet/<name>` com PRG
