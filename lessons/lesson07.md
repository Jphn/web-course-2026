# Aula 7 - Partials de Templates

## Objetivos

- Reutilizar fragmentos de template com `{% include %}`
- Criar macros reutilizáveis com `{% macro %}`
- Construir templates similares a componentes

## Conteúdo (30 min)

1. **Includes**: `{% include 'partials/navbar.html' %}` - insere outro template
2. **Macros**: `{% macro nome(params) %}...{% endmacro %}` - funções reutilizáveis com parâmetros
3. **Importar Macros**: `{% from 'macros.html' import nome %}` ou `{% import 'macros.html' as macros %}`
4. **Casos de Uso**: Flash messages, paginação, cards, campos de formulário

## Prática Guiada (40 min) - Code Along

```html
<!-- templates/partials/flash.html -->
{% with messages = get_flashed_messages(with_categories=true) %} {% if messages
%}
<div class="flash-container">
	{% for category, message in messages %}
	<div class="flash flash-{{ category }}">{{ message }}</div>
	{% endfor %}
</div>
{% endif %} {% endwith %}
```

```html
<!-- templates/macros.html -->
{% macro render_field(name, label, type='text', value='', required=false,
**kwargs) %}
<div class="form-group">
	<label for="{{ name }}">{{ label }}{% if required %} *{% endif %}</label>
	<input
		type="{{ type }}"
		id="{{ name }}"
		name="{{ name }}"
		value="{{ value }}"
		{%
		if
		required
		%}required{%
		endif
		%}
		{{
		kwargs|safe
		}}
	/>
</div>
{% endmacro %} {% macro render_select(name, label, options, value='',
required=false) %}
<div class="form-group">
	<label for="{{ name }}">{{ label }}{% if required %} *{% endif %}</label>
	<select
		id="{{ name }}"
		name="{{ name }}"
		{%
		if
		required
		%}required{%
		endif
		%}
	>
		<option value="">Selecione...</option>
		{% for opt_value, opt_label in options %}
		<option
			value="{{ opt_value }}"
			{%
			if
			opt_value=""
			="value"
			%}selected{%
			endif
			%}
		>
			{{ opt_label }}
		</option>
		{% endfor %}
	</select>
</div>
{% endmacro %} {% macro flash_messages() %} {% with messages =
get_flashed_messages(with_categories=true) %} {% if messages %}
<div class="flash-container">
	{% for category, message in messages %}
	<div class="flash flash-{{ category }}">{{ message }}</div>
	{% endfor %}
</div>
{% endif %} {% endwith %} {% endmacro %}
```

```html
<!-- templates/base.html (atualizado) -->
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{% block title %}Meu App{% endblock %}</title>
		<link
			rel="stylesheet"
			href="{{ url_for('static', filename='css/style.css') }}"
		/>
		{% block head_extra %}{% endblock %}
	</head>
	<body>
		{% include 'partials/navbar.html' %}

		<main class="container">
			{% from 'macros.html' import flash_messages %} {{ flash_messages()
			}} {% block content %}{% endblock %}
		</main>

		{% include 'partials/footer.html' %} {% block scripts %}{% endblock %}
	</body>
</html>
```

```html
<!-- templates/partials/navbar.html -->
<header class="header">
	<div class="logo"><a href="{{ url_for('index') }}">Meu App</a></div>
	<nav class="nav">
		<a href="{{ url_for('index') }}">Home</a>
		<a href="{{ url_for('about') }}">Sobre</a>
		<a href="{{ url_for('contact') }}">Contato</a>
		<a href="{{ url_for('items.list') }}">Itens</a>
	</nav>
</header>
```

```html
<!-- templates/partials/footer.html -->
<footer class="footer">
	<p>&copy; 2024 Meu App</p>
</footer>
```

```html
<!-- templates/items/form.html (usando macros) -->
{% extends 'base.html' %} {% from 'macros.html' import render_field,
render_select %} {% block title %}{{ title }}{% endblock %} {% block content %}
<div class="form-container">
	<h1>{{ title }}</h1>

	<form method="POST" class="form">
		{{ render_field('name', 'Nome', 'text', name or '', true) }} {{
		render_field('description', 'Descrição', 'textarea', description or '',
		false, rows=4) }} {{ render_select('category', 'Categoria',
		[('work','Trabalho'),('personal','Pessoal'),('study','Estudo')],
		category or '', true) }}

		<div class="form-actions">
			<button type="submit" class="btn btn-primary">Salvar</button>
			<a href="{{ url_for('items.list') }}" class="btn btn-secondary"
				>Cancelar</a
			>
		</div>
	</form>
</div>
{% endblock %}
```

## Exercício (10 min)

Criar macro `templates/macros/pagination.html`:

- Parâmetros: `current_page`, `total_pages`, `endpoint`, `query_args`
- Renderizar: links Previous/Next com `url_for(endpoint, page=..., **query_args)`
- Mostrar página atual: "Página X de Y"
- Testar no template de lista de itens

---

## Checklist

- [ ] `partials/navbar.html` e `partials/footer.html` incluídos no base
- [ ] `macros.html` define `render_field`, `render_select`, `flash_messages`
- [ ] Template de formulário usa macros
- [ ] Flash messages funcionam via macro
- [ ] Exercício: macro de paginação criada
