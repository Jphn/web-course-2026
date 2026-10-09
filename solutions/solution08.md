# Solução 8 - Flask Básico

## app/routes/main.py

```python
@main_bp.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

## templates/hello.html

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

Visitar `http://localhost:5000/hello/World` → renderiza "Hello, World!"

## Pontos Principais

- Regra de variável `<name>` captura segmento da URL
- Passado para template como parâmetro `name`
- Template estende layout base
- Usa `url_for` para navegação
