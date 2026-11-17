# Exercício 7 - Partials e macros

## Objetivo

Criar uma macro pequena e reutilizável para exibir categorias em uma página
estática de exemplo. Ainda não use banco de dados ou a rota de itens.

## Instruções

1. Em `templates/macros.html`, adicione:

```html
<!-- templates/macros.html -->
{% macro render_badge(value, label) %}
<span class="badge badge-{{ value }}">{{ label }}</span>
{% endmacro %}
```

2. Crie `templates/categories.html` e importe a macro.
3. Use a macro três vezes:

```html
<!-- templates/categories.html -->
{% if item.category == 'work' %}
    {{ render_badge(item.category, 'Trabalho') }}
{% elif item.category == 'personal' %}
    {{ render_badge(item.category, 'Pessoal') }}
{% else %}
    {{ render_badge(item.category, 'Estudo') }}
{% endif %}
```

## Teste

Abra `categories.html` e confirme que as três categorias aparecem com estilos
distintos.

## Critério de sucesso

- A macro recebe parâmetros
- A macro é importada corretamente
- A tabela continua renderizando sem duplicar o HTML do badge
