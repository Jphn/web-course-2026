# Solução 12 - SQLite e Models

## app/models.py (adição)

```python
def count_items():
    db = get_db()
    cursor = db.execute('SELECT COUNT(*) as total FROM items')
    return cursor.fetchone()['total']
```

## app/routes/items.py (atualizar rota de listagem)

```python
from ..models import count_items

@items_bp.route('/')
def list():
    return render_template('items/list.html',
        items=list_items(),
        total=count_items())
```

## templates/items/list.html (exibição)

```html
<div class="page-header">
	<h1>Itens <span class="badge">{{ total }}</span></h1>
	<a href="{{ url_for('items.new') }}" class="btn btn-primary">Novo Item</a>
</div>
```

## Resultado

- Função consulta COUNT(*) diretamente
- Retorna inteiro total
- Badge mostra contagem ao vivo
- Atualiza automaticamente ao criar/excluir
