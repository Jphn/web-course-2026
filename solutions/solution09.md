# Solução 9 - Rotas e Métodos HTTP

## app/routes/main.py

```python
@main_bp.route('/greet/<name>', methods=['GET', 'POST'])
def greet(name):
    if request.method == 'POST':
        return redirect(url_for('main.greet', name=name))
    return render_template('greet.html', name=name)
```

## templates/greet.html

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

## Fluxo PRG

1. GET `/greet/Alice` → renderiza saudação
2. Usuário clica "Atualizar via POST" → form POSTa para mesma URL
3. Rota detecta POST → redireciona para GET `/greet/Alice`
4. Browser segue redirect → mostra saudação (sem dados de form no histórico)
5. Usuário pressiona F5 → re-executa GET, não POST

## Verificação

- Aba Network: POST 302 → GET 200
- Sem "Confirm Form Resubmission" no refresh
- URL limpa: `/greet/Alice`
