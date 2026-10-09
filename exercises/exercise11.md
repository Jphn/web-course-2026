# Exercício 11 - Blueprints

## Objetivo

Criar blueprint auth placeholder.

## Instruções

1. Criar `app/routes/auth.py`:

```python
from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return 'Logout (TODO)'

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')
```

2. No `app/__init__.py`, registrar:

```python
from .routes.auth import auth_bp
app.register_blueprint(auth_bp)
```

3. No `templates/partials/navbar.html`, adicionar links:

```html
<a href="{{ url_for('auth.login') }}">Login</a>
<a href="{{ url_for('auth.register') }}">Registrar</a>
```

## Teste

Visitar `/auth/login`, verificar blueprint funciona.

## Critério de Sucesso

- Blueprint criado com prefixo
- Registrado no factory
- Rotas acessíveis
- Links da nav funcionam
