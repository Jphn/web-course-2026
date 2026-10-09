# Solução 7 - Partials de Templates

## templates/macros.html (macro pagination)

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

## templates/items/list.html (uso)

```html
{% from 'macros.html' import pagination %} ... {% if total_pages > 1 %} {{
pagination(page, total_pages, 'items.list', {'q': search}) }} {% endif %}
```

## style.css (adições)

```css
.pagination {
	display: flex;
	align-items: center;
	gap: 1rem;
	margin-top: 1.5rem;
	flex-wrap: wrap;
}
.page-info {
	color: var(--text-muted);
	font-size: 0.875rem;
}
```

## Pontos Principais

- Macro aceita current_page, total_pages, endpoint, query_args
- Usa `url_for` com `**query_args` para preservar parâmetros de busca
- Links Anterior/Próximo condicionais
- Acessível com aria-label
