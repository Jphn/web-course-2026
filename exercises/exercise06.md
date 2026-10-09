# Exercício 6 - Herança de Templates

## Objetivo

Criar página de serviços estendendo template base.

## Instruções

1. Criar `templates/services.html`:

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

2. No `templates/partials/navbar.html`, adicionar link:

```html
<a href="{{ url_for('main.services') }}">Serviços</a>
```

3. No `app/routes/main.py`, adicionar rota:

```python
@main_bp.route('/services')
def services():
    return render_template('services.html')
```

## Teste

Navegar para `/services` pela navbar, verificar página renderiza com layout base.

## Critério de Sucesso

- Estende `base.html`
- Define blocks `title` e `content`
- Link da nav funciona
- Herda header/footer/estilos
