# Aula 6 - Herança de templates

## Pré-requisito

Use os templates e a sintaxe Jinja apresentados na Aula 5. Nesta etapa ainda
não usamos Flask nem `url_for`.

## Objetivos

- criar um layout comum com `{% block %}`;
- usar `{% extends %}` em páginas filhas;
- evitar repetir HTML.

## Template base

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Meu App{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Meu App</h1>
        <nav>
            <a href="index.html">Início</a>
            <a href="about.html">Sobre</a>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer><p>Meu App</p></footer>
</body>
</html>
```

Uma página filha contém apenas o que muda:

```html
<!-- templates/about.html -->
{% extends 'base.html' %}

{% block title %}Sobre{% endblock %}

{% block content %}
<h2>Sobre</h2>
<p>Esta página aproveita o layout comum.</p>
{% endblock %}
```

Os links ainda são caminhos HTML simples. A função `url_for()` será apresentada
quando Flask for introduzido.

## Exercício (10 min)

Crie `services.html` usando o layout base e liste três serviços.

## Checklist

- [ ] `base.html` define `title` e `content`
- [ ] A página filha usa `extends`
- [ ] O cabeçalho e o rodapé não são repetidos
