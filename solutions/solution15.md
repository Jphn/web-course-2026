# Solução 15 - Polimento e Deploy (Exemplo: Paginação)

## app/models.py

```python
def list_items(page=1, per_page=10, search=None):
    db = get_db()
    offset = (page - 1) * per_page

    if search:
        sql = '''SELECT * FROM items
                 WHERE name LIKE ? OR description LIKE ?
                 ORDER BY created_at DESC LIMIT ? OFFSET ?'''
        params = (f'%{search}%', f'%{search}%', per_page, offset)
    else:
        sql = 'SELECT * FROM items ORDER BY created_at DESC LIMIT ? OFFSET ?'
        params = (per_page, offset)

    cursor = db.execute(sql, params)
    return cursor.fetchall()

def count_items(search=None):
    db = get_db()
    if search:
        cursor = db.execute(
            'SELECT COUNT(*) as total FROM items WHERE name LIKE ? OR description LIKE ?',
            (f'%{search}%', f'%{search}%')
        )
    else:
        cursor = db.execute('SELECT COUNT(*) as total FROM items')
    return cursor.fetchone()['total']
```

## app/routes/items.py

```python
@items_bp.route('/')
def list():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('q', '').strip()
    per_page = 10

    items = list_items(page=page, per_page=per_page, search=search if search else None)
    total = count_items(search=search if search else None)
    total_pages = (total + per_page - 1) // per_page

    return render_template('items/list.html',
        items=items,
        page=page,
        total_pages=total_pages,
        total=total,
        search=search)
```

## templates/items/list.html (paginação)

```html
<!-- Formulário de busca (existente) -->
<form method="GET" class="search-form">
	<input
		type="search"
		name="q"
		value="{{ search or '' }}"
		placeholder="Buscar..."
	/>
	<button type="submit" class="btn btn-sm">Buscar</button>
	{% if search %}
	<a href="{{ url_for('items.list') }}" class="btn btn-sm btn-secondary"
		>Limpar</a
	>
	{% endif %}
</form>

<!-- Tabela (existente) -->

<!-- Paginação -->
{% if total_pages > 1 %}
<nav class="pagination" aria-label="Paginação">
	{% if page > 1 %}
	<a
		href="{{ url_for('items.list', page=page-1, q=search) }}"
		class="btn btn-sm"
		>&laquo; Anterior</a
	>
	{% endif %}

	<span class="page-info"
		>Página {{ page }} de {{ total_pages }} ({{ total }} itens)</span
	>

	{% if page < total_pages %}
	<a
		href="{{ url_for('items.list', page=page+1, q=search) }}"
		class="btn btn-sm"
		>Próxima &raquo;</a
	>
	{% endif %}
</nav>
{% endif %}
```

## style.css (adições)

```css
.pagination {
	display: flex;
	align-items: center;
	gap: 1rem;
	margin-top: 1.5rem;
	flex-wrap: wrap;
}
.page-info {
	color: var(--text-muted);
	font-size: 0.875rem;
}
```

## Resultado

- 10 itens por página
- Preserva query de busca nos links de paginação
- Mostra página atual e total
- Navegação Anterior/Próxima
