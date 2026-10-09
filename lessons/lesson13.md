# Aula 13 - Listagem e Criação de Itens

## Objetivos

- Renderizar tabela de itens com loop Jinja2
- Criar página dedicada de criação com formulário
- Lidar com validação e feedback

## Conteúdo (30 min)

1. **Template de Lista**: Tabela com `{% for item in items %}`, links de ação
2. **Rota de Criação**: `/items/new` - GET mostra formulário, POST processa
3. **Template de Formulário**: Reutilizável para criar e editar
4. **Integração Flash**: Global no template base

## Prática Guiada (40 min) - Code Along

```python
# app/routes/items.py (adicionar placeholders edit/delete)
@items_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    item = get_item(id)
    if not item:
        flash('Item não encontrado', 'error')
        return redirect(url_for('items.list'))
    # TODO: implementar na próxima aula
    return 'Editar em breve'

@items_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    item = get_item(id)
    if not item:
        flash('Item não encontrado', 'error')
        return redirect(url_for('items.list'))
    # TODO: implementar na próxima aula
    return 'Excluir em breve'
```

```html
<!-- templates/items/list.html (completo) -->
{% extends 'base.html' %} {% block title %}Itens{% endblock %} {% block content
%}
<div class="page-header">
	<h1>Itens <span class="badge">{{ items|length }}</span></h1>
	<a href="{{ url_for('items.new') }}" class="btn btn-primary">Novo Item</a>
</div>

<div class="table-responsive">
	<table class="table">
		<thead>
			<tr>
				<th>Nome</th>
				<th>Categoria</th>
				<th>Descrição</th>
				<th>Criado em</th>
				<th class="actions">Ações</th>
			</tr>
		</thead>
		<tbody>
			{% for item in items %}
			<tr>
				<td>{{ item.name }}</td>
				<td>
					<span class="badge badge-{{ item.category }}"
						>{{ item.category|capitalize }}</span
					>
				</td>
				<td>{{ item.description or '-' }}</td>
				<td>{{ item.created_at[:10] }}</td>
				<td class="actions">
					<a
						href="{{ url_for('items.edit', id=item.id) }}"
						class="btn btn-sm"
						>Editar</a
					>
					<form
						method="POST"
						action="{{ url_for('items.delete', id=item.id) }}"
						class="inline-form"
						onsubmit="return confirm('Excluir este item?')"
					>
						<button type="submit" class="btn btn-sm btn-danger">
							Excluir
						</button>
					</form>
				</td>
			</tr>
			{% else %}
			<tr>
				<td colspan="5" class="empty">Nenhum item cadastrado.</td>
			</tr>
			{% endfor %}
		</tbody>
	</table>
</div>
{% endblock %}
```

```html
<!-- templates/items/form.html (compartilhado create/edit) -->
{% extends 'base.html' %} {% from 'macros.html' import render_field,
render_select %} {% block title %}{{ title }}{% endblock %} {% block content %}
<div class="form-container">
	<h1>{{ title }}</h1>

	<form method="POST" class="form">
		{{ render_field('name', 'Nome', 'text', name or '', true) }} {{
		render_field('description', 'Descrição', 'textarea', description or '',
		false, rows=4) }} {{ render_select('category', 'Categoria',
		[('work','Trabalho'),('personal','Pessoal'),('study','Estudo')],
		category or '', true) }}

		<div class="form-actions">
			<button type="submit" class="btn btn-primary">Salvar</button>
			<a href="{{ url_for('items.list') }}" class="btn btn-secondary"
				>Cancelar</a
			>
		</div>
	</form>

	{% if item %}
	<hr />
	<form
		method="POST"
		action="{{ url_for('items.delete', id=item.id) }}"
		onsubmit="return confirm('Excluir este item?')"
	>
		<button type="submit" class="btn btn-danger">Excluir Item</button>
	</form>
	{% endif %}
</div>
{% endblock %}
```

```css
/* Adicionar ao style.css */
.table-responsive {
	overflow-x: auto;
}
.actions {
	display: flex;
	gap: 0.5rem;
	flex-wrap: wrap;
}
.inline-form {
	display: inline;
}
.btn-sm {
	padding: 0.375rem 0.75rem;
	font-size: 0.8125rem;
}
.btn-danger {
	background: #e74c3c;
}
.btn-danger:hover {
	background: #c0392b;
}
.empty {
	text-align: center;
	color: #999;
	padding: 2rem;
}
.form-container {
	max-width: 600px;
	margin: 0 auto;
}
.form-actions {
	display: flex;
	gap: 1rem;
	margin-top: 1.5rem;
	flex-wrap: wrap;
}
```

## Exercício (10 min)

Adicionar busca à listagem:

- Formulário com método GET, input `name="q"`
- Na rota: `search = request.args.get('q', '').strip()`
- Passar para model: `list_items(search=search)`
- Model: adicionar `WHERE name LIKE ? OR description LIKE ?`

---

## Checklist

- [ ] Página de lista mostra tabela com todos os itens
- [ ] Links de ação usam `url_for('items.edit', id=item.id)`
- [ ] Exclusão usa formulário POST com confirmação JS
- [ ] Página de criação em `/items/new` funciona
- [ ] Template de formulário compartilhado para criar/editar
- [ ] Flash messages aparecem em sucesso/erro
- [ ] Exercício: funcionalidade de busca adicionada
