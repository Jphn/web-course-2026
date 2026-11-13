# Exercício 7 - Partials e macros

## Objetivo

Criar uma macro pequena e reutilizável para exibir categorias.

## Instruções

1. Em `templates/macros.html`, adicione:

```html
{% macro render_badge(value, label) %}
<span class="badge badge-{{ value }}">{{ label }}</span>
{% endmacro %}
```

2. Importe a macro em `templates/items/list.html`.
3. Substitua o badge escrito diretamente na tabela por:

```html
{% if item.category == 'work' %}
    {{ render_badge(item.category, 'Trabalho') }}
{% elif item.category == 'personal' %}
    {{ render_badge(item.category, 'Pessoal') }}
{% else %}
    {{ render_badge(item.category, 'Estudo') }}
{% endif %}
```

## Teste

Visite `/items/` e confirme que as três categorias continuam com estilos
distintos.

## Critério de sucesso

- A macro recebe parâmetros
- A macro é importada corretamente
- A tabela continua renderizando sem duplicar o HTML do badge
