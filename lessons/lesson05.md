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
3. **Renderização**: `render_template('nome.html', variavel=valor)`
4. **Pasta de Templates**: Flask procura em `templates/` por padrão

## Prática Guiada (40 min) - Code Along

```python
# render_demo.py (script standalone para entender renderização)
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
# Rodar
python render_demo.py
```

Agora com Flask:

```python
# app.py (Flask mínimo)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('demo.html', title='Home', user='Alice', items=['Um', 'Dois'])

@app.route('/empty')
def empty():
    return render_template('demo.html', title='Vazio', user=None, items=[])

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercício (10 min)

Criar `templates/profile.html`:

- Estender o conceito: receber dict `user` com `name`, `email`, `role`
- Mostrar "Badge Admin" se `role == 'admin'` usando `{% if %}`
- Loop em `user.skills` lista (array de strings)
- Testar com rota Flask `/profile`

---

## Checklist

- [ ] Sintaxe Jinja2 entendida: `{{ }}`, `{% %}`, `{# #}`
- [ ] Variáveis renderizam no template
- [ ] Condicionais mostram/escondem conteúdo
- [ ] Loops repetem HTML para cada item
- [ ] Flask `render_template` funciona
- [ ] Exercício: `profile.html` com dict e lista
