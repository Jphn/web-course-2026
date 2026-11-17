# Solução 7 - Partials e macros

```html
<!-- templates/macros.html -->
{% macro render_badge(value, label) %}
<span class="badge badge-{{ value }}">{{ label }}</span>
{% endmacro %}
```

Em `templates/categories.html`:

```html
<!-- templates/categories.html -->
{% from 'macros.html' import render_badge %}

{{ render_badge('work', 'Trabalho') }}
{{ render_badge('personal', 'Pessoal') }}
{{ render_badge('study', 'Estudo') }}
```

O CSS das classes `.badge`, `.badge-work`, `.badge-personal` e `.badge-study`
deve ser criado pelo aluno nesta aula.
