# Solução 6 - Herança de Templates

## templates/services.html

```html
{% extends 'base.html' %} {% block title %}Serviços{% endblock %} {% block
content %}
<div class="card">
	<h2>Nossos Serviços</h2>
	<ul>
		<li>Desenvolvimento Web</li>
		<li>Design de API</li>
		<li>Modelagem de Banco</li>
	</ul>
</div>
{% endblock %}
```

## templates/partials/navbar.html (adição)

```html
<nav class="nav">
	<a href="{{ url_for('main.index') }}">Home</a>
	<a href="{{ url_for('main.about') }}">Sobre</a>
	<a href="{{ url_for('main.contact') }}">Contato</a>
	<a href="{{ url_for('main.services') }}">Serviços</a>
</nav>
```

## app/routes/main.py (adição)

```python
@main_bp.route('/services')
def services():
    return render_template('services.html')
```

## Resultado

- Página herda header, footer, estilos do base
- Só define conteúdo único no block `content`
- Navegação acessível de todas as páginas
