# Exercício 8 - Flask Básico

## Objetivo

Adicionar rota dinâmica de hello.

## Instruções

1. No `app/routes/main.py`, adicionar:

```python
@main_bp.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

2. Criar `templates/hello.html`:

```html
{% extends 'base.html' %} {% block title %}Hello {{ name }}{% endblock %} {%
block content %}
<div class="card">
	<h2>Hello, {{ name }}!</h2>
	<p>Bem-vindo ao nosso app Flask.</p>
	<a href="{{ url_for('main.index') }}" class="btn btn-secondary"
		>Voltar ao Home</a
	>
</div>
{% endblock %}
```

## Teste

Visitar `/hello/World`, verificar template renderiza com nome.

## Critério de Sucesso

- Rota aceita parâmetro variável
- Template recebe e exibe variável
- Estende layout base
- Usa `url_for` para navegação
