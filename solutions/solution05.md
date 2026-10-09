# Solução 5 - Jinja2 Básico

## templates/profile.html

```html
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<title>{{ user.name }} - Perfil</title>
	</head>
	<body>
		<h1>{{ user.name }}</h1>
		<p>Email: {{ user.email }}</p>

		{% if user.role == 'admin' %}
		<span class="badge badge-admin">Admin</span>
		{% endif %}

		<h2>Habilidades</h2>
		{% if user.skills %}
		<ul>
			{% for skill in user.skills %}
			<li>{{ skill }}</li>
			{% endfor %}
		</ul>
		{% else %}
		<p>Nenhuma habilidade listada.</p>
		{% endif %}
	</body>
</html>
```

## app.py (rota)

```python
@app.route('/profile')
def profile():
    user = {
        'name': 'Alice',
        'email': 'alice@example.com',
        'role': 'admin',
        'skills': ['Python', 'Flask', 'HTML', 'CSS']
    }
    return render_template('profile.html', user=user)
```

## Conceitos Principais

- Acesso a dict: `user.name`, `user.email`, `user.role`
- Condicional: `{% if user.role == 'admin' %}`
- Loop: `{% for skill in user.skills %}`
- Verificação de vazio: `{% if user.skills %}` antes do loop
