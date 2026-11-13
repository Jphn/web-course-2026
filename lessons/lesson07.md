# Aula 7 - Partials e macros de templates

## Objetivos

- Reutilizar fragmentos de template com `{% include %}`
- Criar macros reutilizáveis com `{% macro %}`
- Separar responsabilidades visuais sem duplicar HTML

## Conteúdo (30 min)

1. **Includes**: inserir navbar e footer compartilhados.
2. **Macros**: criar componentes com parâmetros.
3. **Importação**: usar `{% from 'macros.html' import nome %}`.
4. **Escopo**: manter nomes de variáveis e arquivos em inglês no código; textos
   exibidos ao usuário ficam em pt-BR.

## Prática guiada (40 min)

Crie `templates/macros.html`:

```html
{% macro render_field(name, label, type='text', value='', required=false) %}
<div class="form-group">
    <label for="{{ name }}">{{ label }}{% if required %} *{% endif %}</label>
    <input type="{{ type }}" id="{{ name }}" name="{{ name }}"
           value="{{ value }}" {% if required %}required{% endif %}>
</div>
{% endmacro %}

{% macro flash_messages() %}
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
    <div class="flash-container">
        {% for category, message in messages %}
        <div class="flash flash-{{ category }}">{{ message }}</div>
        {% endfor %}
    </div>
    {% endif %}
{% endwith %}
{% endmacro %}
```

No `base.html`, importe e renderize `flash_messages`. No formulário, use:

```html
{{ render_field('name', 'Nome', 'text', name or '', true) }}
```

Não use sintaxe `**kwargs` na declaração de macros Jinja. Para esta aula,
mantenha os parâmetros explícitos.

## Exercício (10 min)

Crie uma macro `render_badge(value, label)` e use-a na tabela de itens para
exibir a categoria. Teste também uma lista vazia e uma mensagem de feedback.

## Checklist

- [ ] Navbar e footer são incluídos pelo template base
- [ ] `macros.html` define pelo menos duas macros
- [ ] O formulário usa uma macro de campo
- [ ] Flash messages aparecem sem duplicação de HTML
- [ ] Textos visíveis estão em pt-BR
