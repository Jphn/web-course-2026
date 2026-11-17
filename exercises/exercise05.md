# Exercício 5 - Jinja2 Básico

## Objetivo

Criar template de perfil com dict e lista.

## Instruções

1. Criar `templates/profile.html`:

```html
<!-- templates/profile.html -->
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
		<p>Perfil de administradora</p>
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

2. No `render_demo.py`, crie um dicionário:

```python
# render_demo.py
user = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'role': 'admin',
    'skills': ['Python', 'Flask', 'HTML', 'CSS']
}
template = env.get_template('profile.html')
print(template.render(user=user))
```

## Teste

Executar `python render_demo.py` e verificar todos os dados renderizados.

## Critério de Sucesso

- Valores de dict acessados com `user.chave`
- Condicional mostra badge admin
- Loop renderiza todas skills
