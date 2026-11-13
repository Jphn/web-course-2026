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
	<a href="{{ url_for('index') }}">Início</a>
	<a href="{{ url_for('about') }}">Sobre</a>
	<a href="{{ url_for('contact') }}">Contato</a>
	<a href="{{ url_for('services') }}">Serviços</a>
</nav>
```

## app/routes.py (adição)

```python
@app.route('/services')
def services():
    return render_template('services.html')
```

## Resultado

- Página herda header, footer, estilos do base
- Só define conteúdo único no block `content`
- Navegação acessível de todas as páginas
