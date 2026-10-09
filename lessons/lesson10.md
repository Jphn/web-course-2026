# Aula 10 - Tratamento de Formulários

## Objetivos

- Acessar dados do formulário com `request.form`
- Validar no server side
- Mostrar feedback com flash messages
- Repopular formulário após erro de validação

## Conteúdo (30 min)

1. **Dados do Formulário**: `request.form.get('campo')` retorna string ou `None`
2. **Validação Server-Side**: Nunca confiar no cliente; validar no Python
3. **Flash Messages**: `flash('mensagem', 'categoria')` + `get_flashed_messages(with_categories=true)`
4. **Categorias**: `'success'`, `'error'`, `'warning'`, `'info'`
5. **Repopulação**: Passar valores de volta ao template: `value="{{ name or '' }}"`

## Prática Guiada (40 min) - Code Along

```python
# app/routes/items.py (atualizado)
from flask import Blueprint, render_template, request, redirect, url_for, flash

items_bp = Blueprint('items', __name__, url_prefix='/items')

ITEMS = []

@items_bp.route('/', methods=['GET', 'POST'])
def list_items():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()

        errors = []
        if not name:
            errors.append('Nome é obrigatório')
        elif len(name) > 100:
            errors.append('Nome muito longo (máx 100 chars)')
        if not category:
            errors.append('Categoria é obrigatória')
        elif category not in ['work', 'personal', 'study']:
            errors.append('Categoria inválida')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('items/list.html',
                items=ITEMS, name=name, category=category), 400

        ITEMS.append({'id': len(ITEMS) + 1, 'name': name, 'category': category})
        flash(f'Item "{name}" criado!', 'success')
        return redirect(url_for('items.list_items'))

    return render_template('items/list.html', items=ITEMS)
```

```html
<!-- templates/items/list.html (atualizado com flash e formulário) -->
{% extends 'base.html' %} {% from 'macros.html' import render_field,
render_select %} {% block title %}Itens{% endblock %} {% block content %}
<div class="page-header">
	<h1>Itens</h1>
</div>

<form method="POST" class="form">
	{{ render_field('name', 'Nome', 'text', name or '', true) }} {{
	render_select('category', 'Categoria',
	[('work','Trabalho'),('personal','Pessoal'),('study','Estudo')], category or
	'', true) }}
	<button type="submit" class="btn btn-primary">Adicionar</button>
</form>

{% if items %}
<table class="table">
	<thead>
		<tr>
			<th>ID</th>
			<th>Nome</th>
			<th>Categoria</th>
		</tr>
	</thead>
	<tbody>
		{% for item in items %}
		<tr>
			<td>{{ item.id }}</td>
			<td>{{ item.name }}</td>
			<td>
				<span class="badge badge-{{ item.category }}"
					>{{ item.category|capitalize }}</span
				>
			</td>
		</tr>
		{% endfor %}
	</tbody>
</table>
{% else %}
<p>Nenhum item ainda.</p>
{% endif %} {% endblock %}
```

```css
/* Adicionar ao style.css */
.badge {
	display: inline-block;
	padding: 0.25rem 0.75rem;
	border-radius: 9999px;
	font-size: 0.75rem;
	font-weight: 600;
	text-transform: capitalize;
}
.badge-work {
	background: #e3f2fd;
	color: #1565c0;
}
.badge-personal {
	background: #f3e5f5;
	color: #7b1fa2;
}
.badge-study {
	background: #e8f5e9;
	color: #2e7d32;
}
```

## Exercício (10 min)

Adicionar ao formulário:

- Campo `description` (textarea, opcional)
- Validar: se preenchido, máx 500 caracteres
- Armazenar no dict do item e exibir na tabela

---

## Checklist

- [ ] `request.form.get()` usado para todos os campos
- [ ] Validações: obrigatório, tamanho, valores permitidos
- [ ] `flash()` usado para erros e sucesso
- [ ] Formulário repopula com `name or ''` e `category or ''`
- [ ] Flash messages estilizadas no template base
- [ ] Exercício: campo description adicionado
