# Aula 12 - SQLite e Camada de Models

## Objetivos

- Usar módulo `sqlite3` nativo do Python
- Gerenciar conexões de banco por request
- Criar funções de model para operações CRUD

## Conteúdo (30 min)

1. **SQLite**: Baseado em arquivo, zero config, perfeito para aprendizado
2. **Conexão por Request**: Armazenar no `g` do Flask, fechar no teardown
3. **Row Factory**: `sqlite3.Row` para acesso tipo dict
4. **Funções de Model**: `list_items()`, `get_item(id)`, `create_item()`, `update_item()`, `delete_item()`
5. **Segurança**: Queries parametrizadas com placeholders `?`

## Prática Guiada (40 min) - Code Along

```python
# app/models.py
import sqlite3
from flask import g

DB_PATH = 'app.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# --- CRUD ---
def list_items():
    db = get_db()
    cursor = db.execute('SELECT * FROM items ORDER BY created_at DESC')
    return cursor.fetchall()

def get_item(id):
    db = get_db()
    cursor = db.execute('SELECT * FROM items WHERE id = ?', (id,))
    return cursor.fetchone()

def create_item(name, category, description=''):
    db = get_db()
    # Verificar nome único
    exists = db.execute('SELECT 1 FROM items WHERE name = ?', (name,)).fetchone()
    if exists:
        raise ValueError('Item com este nome já existe')

    cursor = db.execute(
        'INSERT INTO items (name, category, description) VALUES (?, ?, ?)',
        (name, category, description)
    )
    db.commit()
    return cursor.lastrowid

def update_item(id, name, category, description):
    db = get_db()
    exists = db.execute('SELECT 1 FROM items WHERE name = ? AND id != ?', (name, id)).fetchone()
    if exists:
        raise ValueError('Item com este nome já existe')

    db.execute(
        'UPDATE items SET name = ?, category = ?, description = ? WHERE id = ?',
        (name, category, description, id)
    )
    db.commit()

def delete_item(id):
    db = get_db()
    db.execute('DELETE FROM items WHERE id = ?', (id,))
    db.commit()
```

```python
# app/routes/items.py (atualizado para usar models)
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import list_items, get_item, create_item, update_item, delete_item

items_bp = Blueprint('items', __name__, url_prefix='/items')

@items_bp.route('/')
def list():
    return render_template('items/list.html', items=list_items())

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

        if errors:
            for e in errors: flash(e, 'error')
            return render_template('items/form.html', title='Novo Item',
                name=name, category=category, description=description), 400

        try:
            create_item(name, category, description)
            flash(f'Item "{name}" criado!', 'success')
            return redirect(url_for('items.list'))
        except ValueError as e:
            flash(str(e), 'error')
            return render_template('items/form.html', title='Novo Item',
                name=name, category=category, description=description), 400

    return render_template('items/form.html', title='Novo Item')
```

## Exercício (10 min)

Adicionar ao `models.py`:

- `count_items()` - retorna total de registros
- Usar no template de listagem para mostrar "X itens total"

---

## Checklist

- [ ] `models.py` com todas funções CRUD
- [ ] `get_db()` usa `g` para conexão por request
- [ ] `close_db()` registrado no teardown
- [ ] `init_db()` cria tabela com constraint UNIQUE no name
- [ ] Queries parametrizadas (`?`) usadas em todo lugar
- [ ] Rotas importam e usam funções de model
- [ ] Exercício: `count_items()` implementado
