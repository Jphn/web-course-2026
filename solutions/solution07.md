# Solução 7 - Partials e macros

```html
{% macro render_badge(value, label) %}
<span class="badge badge-{{ value }}">{{ label }}</span>
{% endmacro %}
```

No início de `templates/items/list.html`:

```html
{% from 'macros.html' import render_badge %}
```

Uso na tabela:

```html
{% if item.category == 'work' %}
    {{ render_badge(item.category, 'Trabalho') }}
{% elif item.category == 'personal' %}
    {{ render_badge(item.category, 'Pessoal') }}
{% else %}
    {{ render_badge(item.category, 'Estudo') }}
{% endif %}
```
