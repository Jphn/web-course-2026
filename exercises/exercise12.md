# Exercício 12 - SQLite e Models

## Objetivo

Adicionar função count_items.

## Instruções

1. No `app/models.py`, adicionar:

```python
def count_items():
    db = get_db()
    cursor = db.execute('SELECT COUNT(*) as total FROM items')
    return cursor.fetchone()['total']
```

2. No `app/routes/items.py`, usar na rota de listagem:

```python
from ..models import count_items

@items_bp.route('/')
def list():
    return render_template('items/list.html',
        items=list_items(),
        total=count_items())
```

3. No `templates/items/list.html`, exibir:

```html
<h1>Itens <span class="badge">{{ total }}</span></h1>
```

## Teste

Visitar `/items`, verificar badge mostra contagem correta.

## Critério de Sucesso

- Função retorna inteiro com total
- Passado para template
- Exibido no badge
- Atualiza ao criar/excluir
