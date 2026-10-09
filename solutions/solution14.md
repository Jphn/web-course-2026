# Solução 14 - Edição e Exclusão

## templates/items/form.html (form-actions atualizado)

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

## Comportamento

- **Modo criação** (`/items/new`): `item` é None/undefined
    - Mostra: Salvar, Cancelar
- **Modo edição** (`/items/1/edit`): `item` existe
    - Mostra: Salvar, Cancelar, Voltar à Lista

## Resultado

- Renderização condicional com `{% if item %}`
- Estilização de botão consistente
- Opções claras de navegação
