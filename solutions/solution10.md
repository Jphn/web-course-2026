# Solução 10 - Tratamento de Formulários

## templates/items/form.html (adição)

```html
{{ render_field('description', 'Descrição', 'textarea', description or '',
false, rows=4) }}
```

## app/routes/items.py (atualizações)

```python
@items_bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()

        errors = []
        if not name: errors.append('Nome é obrigatório')
        elif len(name) > 100: errors.append('Nome muito longo')
        if not category: errors.append('Categoria é obrigatória')
        elif category not in ['work', 'personal', 'study']: errors.append('Categoria inválida')
        if description and len(description) > 500:
            errors.append('Descrição muito longa (máx 500 chars)')

        if errors:
            for e in errors: flash(e, 'error')
            return render_template('items/form.html', title='Novo Item',
                name=name, category=category, description=description), 400

        create_item(name, category, description)
        flash(f'Item "{name}" criado!', 'success')
        return redirect(url_for('items.list'))

    return render_template('items/form.html', title='Novo Item')
```

## app/models.py (assinatura create_item)

```python
def create_item(name, category, description=''):
    # ... código existente ...
    cursor = db.execute(
        'INSERT INTO items (name, category, description) VALUES (?, ?, ?)',
        (name, category, description)
    )
    # ...
```

## templates/items/list.html (coluna da tabela)

```html
<th>Descrição</th>
...
<td>{{ item.description or '-' }}</td>
```

## Resultado

- Description opcional, máx 500 chars
- Armazenado no banco
- Exibido na tabela de listagem
- Repopula em erro de validação
