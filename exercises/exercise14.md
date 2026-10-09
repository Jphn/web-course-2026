# Exercício 14 - Edição e Exclusão

## Objetivo

Adicionar botão "Voltar à Lista" no formulário de edição.

## Instruções

1. No `templates/items/form.html`, atualizar form-actions:

```html
<div class="form-actions">
	<button type="submit" class="btn btn-primary">Salvar</button>
	<a href="{{ url_for('items.list') }}" class="btn btn-secondary">Cancelar</a>
	{% if item %}
	<a href="{{ url_for('items.list') }}" class="btn btn-secondary"
		>Voltar à Lista</a
	>
	{% endif %}
</div>
```

## Teste

- Visitar `/items/1/edit` → vê botão "Voltar à Lista"
- Visitar `/items/novo` → NÃO vê botão "Voltar à Lista"

## Critério de Sucesso

- Botão só no modo edição (`item` existe)
- Link leva para listagem
- Estilização consistente
