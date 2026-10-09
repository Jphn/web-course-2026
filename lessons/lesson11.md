# Aula 11 - Blueprints e Estrutura do Projeto

## Objetivos

- Organizar rotas em Blueprints
- Usar padrão Application Factory
- Estruturar projeto para crescimento

## Conteúdo (30 min)

1. **Blueprint**: Mini-app com próprias rotas, templates, static
2. **Registro**: `app.register_blueprint(bp, url_prefix='/prefix')`
3. **Factory Pattern**: `create_app()` cria e configura app
4. **Estrutura do Projeto**:
    ```
    app/
    ├── __init__.py          # create_app()
    ├── models.py            # camada de banco
    ├── routes/
    │   ├── __init__.py
    │   ├── main.py          # home, about, contact
    │   └── items.py         # rotas CRUD
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── items/
    │   │   ├── list.html
    │   │   └── form.html
    │   └── partials/
    └── static/
        └── css/style.css
    ```

## Prática Guiada (40 min) - Code Along

```python
# app/__init__.py (refatorado)
import os
from flask import Flask
from .models import init_db, close_db

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    from .routes.main import main_bp
    from .routes.items import items_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp)

    return app
```

```python
# app/routes/main.py (inalterado)
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
```

```python
# app/routes/items.py (atualizado com prefixo do blueprint)
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import list_items, create_item

items_bp = Blueprint('items', __name__, url_prefix='/items')

@items_bp.route('/')
def list():
    return render_template('items/list.html', items=list_items())

@items_bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        # ... validações iguais às anteriores ...
        try:
            create_item(name, category)
            flash(f'Item "{name}" criado!', 'success')
            return redirect(url_for('items.list'))
        except ValueError as e:
            flash(str(e), 'error')

    return render_template('items/form.html', title='Novo Item')
```

```html
<!-- templates/items/list.html (atualizar url_for) -->
<a href="{{ url_for('items.new') }}" class="btn btn-primary">Novo Item</a>
```

## Exercício (10 min)

Criar `app/routes/auth.py` blueprint:

- Rotas: `/login` (GET), `/logout` (POST), `/register` (GET/POST)
- Registrar no `create_app()` com `url_prefix='/auth'`
- Adicionar links login/register na navbar partial

---

## Checklist

- [ ] Pacote `app/routes/` com `__init__.py`
- [ ] `main_bp` e `items_bp` criados
- [ ] `url_prefix='/items'` no blueprint de itens
- [ ] `create_app()` registra ambos blueprints
- [ ] Templates usam `url_for('items.list')`, `url_for('items.new')`
- [ ] App roda sem erros
- [ ] Exercício: blueprint `auth.py` criado
