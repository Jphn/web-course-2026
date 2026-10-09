# Exercício 5 - Jinja2 Básico

## Objetivo

Criar template de perfil com dict e lista.

## Instruções

1. Criar `templates/profile.html`:

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

2. Adicionar rota no `app.py`:

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

## Teste

Visitar `/profile`, verificar todos dados renderizam.

## Critério de Sucesso

- Valores de dict acessados com `user.chave`
- Condicional mostra badge admin
- Loop renderiza todas skills
