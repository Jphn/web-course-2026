# Aula 6 - Herança de Templates

## Objetivos

- Criar layout base com blocks
- Estender base em templates filhos
- Aplicar princípio DRY (Don't Repeat Yourself)

## Conteúdo (30 min)

1. **Template Base**: Estrutura comum (head, header, footer) com `{% block nome %}{% endblock %}`
2. **Templates Filhos**: `{% extends 'base.html' %}` + sobrescrever blocks
3. **Tipos de Blocks**:
    - Blocks obrigatórios: devem ser preenchidos
    - Blocks opcionais: conteúdo padrão com `{{ super() }}`
4. **Múltiplos Blocks**: `title`, `head_extra`, `content`, `scripts`

## Prática Guiada (40 min) - Code Along

```html
<!-- templates/base.html -->
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
		<header class="header">
			<div class="logo"><a href="{{ url_for('index') }}">Meu App</a></div>
			<nav class="nav">
				<a href="{{ url_for('index') }}">Home</a>
				<a href="{{ url_for('about') }}">Sobre</a>
				<a href="{{ url_for('contact') }}">Contato</a>
			</nav>
		</header>

		<main class="container">
			{% block flash %}{% endblock %} {% block content %}{% endblock %}
		</main>

		<footer class="footer">
			<p>&copy; 2024 Meu App</p>
		</footer>

		{% block scripts %}{% endblock %}
	</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends 'base.html' %} {% block title %}Home{% endblock %} {% block content
%}
<div class="card">
	<h2>Bem-vindo ao Meu App</h2>
	<p>Esta é a home page usando herança de templates.</p>
	<a href="{{ url_for('about') }}" class="btn">Saiba Mais</a>
</div>
{% endblock %}
```

```html
<!-- templates/about.html -->
{% extends 'base.html' %} {% block title %}Sobre{% endblock %} {% block content
%}
<div class="card">
	<h2>Sobre Nós</h2>
	<p>Construímos aplicações web simples com Python e Flask.</p>
</div>
{% endblock %}
```

```html
<!-- templates/contact.html -->
{% extends 'base.html' %} {% block title %}Contato{% endblock %} {% block
content %}
<div class="card">
	<h2>Contato</h2>
	<p>Email: <a href="mailto:hello@example.com">hello@example.com</a></p>
</div>
{% endblock %}
```

```python
# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercício (10 min)

Criar `templates/services.html`:

- Estender `base.html`
- Block `title`: "Serviços"
- Block `content`: Listar 3 serviços usando `<ul>` com `<li>`
- Adicionar link na nav do base.html para `/services`
- Testar navegação

---

## Checklist

- [ ] `base.html` define blocks: title, head_extra, content, scripts
- [ ] Templates filhos usam `{% extends 'base.html' %}`
- [ ] Navegação funciona entre todas as páginas
- [ ] CSS ainda aplica (static files via `url_for`)
- [ ] Exercício: `services.html` criado e linkado
