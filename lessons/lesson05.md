# Aula 5 - Jinja2 Básico

## Objetivos

- Entender conceito de template engine
- Usar variáveis, condicionais, loops em templates
- Renderizar templates a partir do Python

## Conteúdo (30 min)

1. **Por que Templates?**: Separar lógica de apresentação, reutilizar HTML
2. **Sintaxe Jinja2**:
    - `{{ variavel }}` - imprime valor
    - `{% if condicao %}...{% endif %}`
    - `{% for item in lista %}...{% endfor %}`
    - `{# comentario #}`
3. **Renderização**: carregar um arquivo e chamar `template.render(...)`
4. **Pasta de Templates**: organizar os arquivos em `templates/`

## Prática Guiada (40 min) - Code Along

```python
# render_demo.py (script standalone)
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

# Variáveis
template = env.get_template('demo.html')
print(template.render(title='Olá', user='Alice', items=['Maçã', 'Banana', 'Cereja']))

# Condicionais
print(template.render(title='Dashboard', user=None, items=[]))
```

```html
<!-- templates/demo.html -->
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<title>{{ title }}</title>
	</head>
	<body>
		<h1>{{ title }}</h1>

		{% if user %}
		<p>Bem-vindo, {{ user }}!</p>
		{% else %}
		<p>Por favor, faça login.</p>
		{% endif %}

		<h2>Itens</h2>
		{% if items %}
		<ul>
			{% for item in items %}
			<li>{{ item }}</li>
			{% endfor %}
		</ul>
		{% else %}
		<p>Nenhum item encontrado.</p>
		{% endif %}
	</body>
</html>
```

```bash
# terminal
# Instalar a biblioteca usada nesta demonstração
pip install Jinja2

# Rodar
python render_demo.py
```

## Exercício (10 min)

Criar `templates/profile.html`:

- Estender o conceito: receber dict `user` com `name`, `email`, `role`
- Mostrar "Badge Admin" se `role == 'admin'` usando `{% if %}`
- Loop em `user.skills` lista (array de strings)
- Renderizar o template com o mesmo script, passando um novo dicionário

---

## Checklist

- [ ] Sintaxe Jinja2 entendida: `{{ }}`, `{% %}`, `{# #}`
- [ ] Variáveis renderizam no template
- [ ] Condicionais mostram/escondem conteúdo
- [ ] Loops repetem HTML para cada item
- [ ] O template renderiza variáveis, condicionais e loops
- [ ] Exercício: `profile.html` com dict e lista
