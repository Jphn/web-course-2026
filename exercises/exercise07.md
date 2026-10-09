# Exercício 7 - Partials de Templates

## Objetivo

Criar macro de paginação.

## Instruções

1. No `templates/macros.html`, adicionar:

```html
{% macro pagination(current_page, total_pages, endpoint, query_args={}) %}
<nav class="pagination" aria-label="Paginação">
	{% if current_page > 1 %}
	<a
		href="{{ url_for(endpoint, page=current_page-1, **query_args) }}"
		class="btn btn-sm"
		>&laquo; Anterior</a
	>
	{% endif %}

	<span class="page-info"
		>Página {{ current_page }} de {{ total_pages }}</span
	>

	{% if current_page < total_pages %}
	<a
		href="{{ url_for(endpoint, page=current_page+1, **query_args) }}"
		class="btn btn-sm"
		>Próxima &raquo;</a
	>
	{% endif %}
</nav>
{% endmacro %}
```

2. No `templates/items/list.html`, usar:

```html
{% from 'macros.html' import pagination %} ... {{ pagination(page, total_pages,
'items.list') }}
```

3. Atualizar rota para aceitar parâmetro page (placeholder por enquanto)

## Teste

Visitar `/items`, verificar paginação renderiza (mesmo que não funcional ainda).

## Critério de Sucesso

- Macro definida com parâmetros
- Gera links `url_for` corretos
- Renderiza no template de lista
