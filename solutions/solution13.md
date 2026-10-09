# Solução 13 - Listagem e Criação

## templates/items/list.html (formulário de busca)

```html
<form method="GET" class="search-form">
	<input
		type="search"
		name="q"
		value="{{ search or '' }}"
		placeholder="Buscar itens..."
	/>
	<button type="submit" class="btn btn-sm">Buscar</button>
	{% if search %}
	<a href="{{ url_for('items.list') }}" class="btn btn-sm btn-secondary"
		>Limpar</a
	>
	{% endif %}
</form>
```

## app/routes/items.py (atualizar listagem)

```python
@items_bp.route('/')
def list():
    search = request.args.get('q', '').strip()
    return render_template('items/list.html',
        items=list_items(search=search if search else None),
        search=search)
```

## app/models.py (atualizar list_items)

```python
def list_items(search=None):
    db = get_db()
    if search:
        cursor = db.execute(
            'SELECT * FROM items WHERE name LIKE ? OR description LIKE ? ORDER BY created_at DESC',
            (f'%{search}%', f'%{search}%')
        )
    else:
        cursor = db.execute('SELECT * FROM items ORDER BY created_at DESC')
    return cursor.fetchall()
```

## style.css (adições)

```css
.search-form {
	display: flex;
	gap: 0.5rem;
	margin-bottom: 1.5rem;
	flex-wrap: wrap;
}
.search-form input {
	flex: 1;
	min-width: 200px;
}
```

## Resultado

- Formulário GET preserva busca na URL
- Busca por nome E descrição
- Case-insensitive (SQLite LIKE padrão)
- Link limpar reseta para lista completa
