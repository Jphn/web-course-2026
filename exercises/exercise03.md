# Exercício 3 - Formulários HTML

## Objetivo

Adicionar inputs de data e arquivo ao formulário.

## Instruções

1. No `form.html`, adicionar após select de categoria:

```html
<div class="form-group">
	<label for="due_date">Data de Vencimento</label>
	<input type="date" id="due_date" name="due_date" />
</div>

<div class="form-group">
	<label for="attachment">Anexo</label>
	<input type="file" id="attachment" name="attachment" />
</div>
```

2. Estilizar consistentemente no `style.css`

## Teste

Abrir `form.html` no browser, verificar novos campos aparecem e estão estilizados.

## Critério de Sucesso

- Date picker abre calendário nativo
- File selector abre dialog do SO
- Estilização consistente com outros campos
