# Aula 14 - Edição e Exclusão de Itens

## Objetivos

- Implementar edição: GET pré-preenche formulário, POST atualiza
- Implementar exclusão: apenas POST com confirmação
- Manter padrão PRG em tudo

## Conteúdo (30 min)

1. **Rota de Edição**: `/items/<id>/edit`
    - GET: `get_item(id)` → pré-preencher formulário
    - POST: validar → `update_item()` → flash → redirect
2. **Rota de Exclusão**: `/items/<id>/delete` (apenas POST)
    - Segurança: nunca DELETE via GET
    - Confirmação: JS `confirm()` ou página intermediária
3. **Reuso de Formulário**: Mesmo `form.html` para criar e editar

## Prática Guiada (40 min) - Code Along

```python
# app/routes/items.py (edit/delete completos)

@items_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    item = get_item(id)
    if not item:
        flash('Item não encontrado', 'error')
        return redirect(url_for('items.list'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()

        errors = []
        if not name: errors.append('Nome é obrigatório')
        elif len(name) > 100: errors.append('Nome muito longo')
        if not category: errors.append('Categoria é obrigatória')
        elif category not in ['work', 'personal', 'study']: errors.append('Categoria inválida')

        if errors:
            for e in errors: flash(e, 'error')
            return render_template('items/form.html', title='Editar Item', item=item,
                name=name, category=category, description=description), 400

        try:
            update_item(id, name, category, description)
            flash(f'Item "{name}" atualizado!', 'success')
            return redirect(url_for('items.list'))
        except ValueError as e:
            flash(str(e), 'error')
            return render_template('items/form.html', title='Editar Item', item=item,
                name=name, category=category, description=description), 400

    # GET: pré-preenche com dados atuais
    return render_template('items/form.html', title='Editar Item', item=item,
        name=item.name, category=item.category, description=item.description)

@items_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    item = get_item(id)
    if not item:
        flash('Item não encontrado', 'error')
        return redirect(url_for('items.list'))

    name = item.name
    delete_item(id)
    flash(f'Item "{name}" excluído!', 'success')
    return redirect(url_for('items.list'))
```

```html
<!-- templates/items/form.html (detecta edição via variável `item`) -->
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

## Exercício (10 min)

Adicionar botão "Voltar à Lista" no formulário de edição (ao lado do Cancelar):

- Só aparece quando `item` existe (modo edição)
- Linka para `url_for('items.list')`
- Mesmo estilo do botão Cancelar

---

## Checklist

- [ ] Edição GET pré-preenche formulário com dados do item
- [ ] Edição POST valida e atualiza banco
- [ ] Exclusão aceita apenas POST
- [ ] Ambos mostram flash success e redirecionam para lista
- [ ] Confirmação de exclusão funciona (JS confirm)
- [ ] Formulário detecta modo edição via `{% if item %}`
- [ ] Exercício: botão "Voltar à Lista" adicionado
