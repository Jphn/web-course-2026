# Exercício 13 - Listagem e Criação

## Objetivo

Adicionar busca à listagem de itens.

## Instruções

1. No `templates/items/list.html`, adicionar formulário de busca acima da tabela:

```html
<form method="GET" class="search-form">
	<input
		type="search"
		name="q"
		value="{{ request.args.get('q', '') }}"
		placeholder="Buscar..."
	/>
	<button type="submit" class="btn btn-sm">Buscar</button>
	{% if request.args.get('q') %}
	<a href="{{ url_for('items.list') }}" class="btn btn-sm btn-secondary"
		>Limpar</a
	>
	{% endif %}
</form>
```

2. No `app/routes/items.py`, atualizar rota de listagem:

```python
@items_bp.route('/')
def list():
    search = request.args.get('q', '').strip()
    return render_template('items/list.html',
        items=list_items(search=search if search else None),
        search=search)
```

3. No `app/models.py`, atualizar list_items:

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

## Teste

Buscar por nome de item existente, verificar resultados filtrados.

## Critério de Sucesso

- Formulário de busca usa GET
- Filtra por nome E descrição
- Link limpar remove filtro
- Busca vazia mostra todos
