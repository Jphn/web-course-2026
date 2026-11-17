# Aula 7 - Includes e macros de templates

## Pré-requisito

Esta aula continua usando os templates da Aula 6. Flask, formulários enviados
ao servidor e mensagens flash serão ensinados depois.

## Objetivos

- reutilizar fragmentos com `{% include %}`;
- criar macros com parâmetros;
- estilizar os componentes que forem criados nesta aula.

## Includes

Separe partes repetidas em arquivos:

```html
<!-- templates/partials/footer.html -->
<footer>
    <p>Meu App</p>
</footer>
```

Depois, inclua o arquivo no template base:

```html
<!-- templates/base.html -->
{% include 'partials/footer.html' %}
```

## Macro de campo

```html
<!-- templates/macros.html -->
{% macro render_field(name, label, type='text', value='', required=false) %}
<div class="form-group">
    <label for="{{ name }}">{{ label }}{% if required %} *{% endif %}</label>
    <input type="{{ type }}" id="{{ name }}" name="{{ name }}"
           value="{{ value }}" {% if required %}required{% endif %}>
</div>
{% endmacro %}
```

Importe e use a macro:

```html
<!-- templates/index.html -->
{% from 'macros.html' import render_field %}
{{ render_field('name', 'Nome', required=true) }}
```

## CSS criado nesta aula

Uma macro gera HTML, mas não cria estilos. A classe `.form-group` já foi
estilizada na Aula 3; reutilize aquele CSS em vez de criá-lo novamente.

Para o exercício desta aula, adicione ao `style.css` as classes de categoria:

```css
/* static/css/style.css */
.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-weight: 600;
}

.badge-work { background: #e3f2fd; color: #1565c0; }
.badge-personal { background: #f3e5f5; color: #7b1fa2; }
.badge-study { background: #e8f5e9; color: #2e7d32; }
```

As classes de mensagens (`flash-*`) ainda não aparecem aqui. Elas dependem de
`flash()` do Flask e serão criadas junto com as mensagens na Aula 11.

## Exercício (10 min)

Crie uma macro `render_badge(value, label)` e o CSS de `.badge`. Use-a em uma
página de exemplo com três categorias, sem depender ainda do banco de dados.

## Checklist

- [ ] Um fragmento é incluído com `include`
- [ ] Uma macro é importada e chamada
- [ ] As classes usadas pela macro estão estilizadas
- [ ] O exercício funciona sem Flask ou banco de dados
