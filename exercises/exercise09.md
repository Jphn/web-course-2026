# Exercício 9 - Rotas e Métodos HTTP

## Objetivo

Criar rota greet com padrão PRG.

## Instruções

1. No `app/routes/main.py`, adicionar:

```python
@main_bp.route('/greet/<name>', methods=['GET', 'POST'])
def greet(name):
    if request.method == 'POST':
        return redirect(url_for('main.greet', name=name))
    return render_template('greet.html', name=name)
```

2. Criar `templates/greet.html`:

```html
{% extends 'base.html' %} {% block title %}Greet {{ name }}{% endblock %} {%
block content %}
<div class="card">
	<h2>Hello, {{ name }}!</h2>
	<form method="POST">
		<button type="submit" class="btn btn-primary">
			Atualizar via POST
		</button>
	</form>
	<p><a href="{{ url_for('main.index') }}">Voltar ao Home</a></p>
</div>
{% endblock %}
```

## Teste

- GET `/greet/Alice` → mostra saudação
- Clicar "Atualizar via POST" → redireciona para GET (sem reenvio de formulário no F5)

## Critério de Sucesso

- Rota lida GET e POST
- POST redireciona para GET (PRG)
- Sem reenvio duplicado no refresh
