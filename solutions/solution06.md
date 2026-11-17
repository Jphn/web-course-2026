# Solução 6 - Herança de templates

## `templates/services.html`

```html
<!-- templates/services.html -->
{% extends 'base.html' %}

{% block title %}Serviços{% endblock %}

{% block content %}
<div class="card">
    <h2>Nossos serviços</h2>
    <ul>
        <li>Desenvolvimento web</li>
        <li>Design de páginas</li>
        <li>Organização de conteúdo</li>
    </ul>
</div>
{% endblock %}
```

No menu do `base.html`, o link pode ser:

```html
<!-- templates/base.html -->
<a href="services.html">Serviços</a>
```
