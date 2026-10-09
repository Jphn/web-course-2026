# Solução 11 - Blueprints

## app/routes/auth.py

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

## app/**init**.py

```python
def create_app():
    # ... código existente ...
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app
```

## templates/partials/navbar.html

```html
<nav class="nav">
	<a href="{{ url_for('main.index') }}">Home</a>
	<a href="{{ url_for('main.about') }}">Sobre</a>
	<a href="{{ url_for('main.contact') }}">Contato</a>
	<a href="{{ url_for('items.list') }}">Itens</a>
	<a href="{{ url_for('auth.login') }}">Login</a>
	<a href="{{ url_for('auth.register') }}">Registrar</a>
</nav>
```

## templates/auth/login.html (básico)

```html
{% extends 'base.html' %} {% block title %}Login{% endblock %} {% block content
%}
<div class="card">
	<h2>Login</h2>
	<form method="POST">
		{{ render_field('username', 'Usuário', 'text', '', true) }} {{
		render_field('password', 'Senha', 'password', '', true) }}
		<button type="submit" class="btn btn-primary">Login</button>
	</form>
</div>
{% endblock %}
```

## templates/auth/register.html (básico)

```html
{% extends 'base.html' %} {% block title %}Registrar{% endblock %} {% block
content %}
<div class="card">
	<h2>Registrar</h2>
	<form method="POST">
		{{ render_field('username', 'Usuário', 'text', '', true) }} {{
		render_field('email', 'Email', 'email', '', true) }} {{
		render_field('password', 'Senha', 'password', '', true) }}
		<button type="submit" class="btn btn-primary">Registrar</button>
	</form>
</div>
{% endblock %}
```

## Resultado

- Blueprint no prefixo `/auth`
- Rotas: `/auth/login`, `/auth/logout`, `/auth/register`
- Templates em `templates/auth/`
- Links da navbar usam `url_for('auth.login')`
