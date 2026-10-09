# Solução 3 - Formulários HTML

## form.html (adições)

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

## style.css (já lida com estes via seletor .form-group input existente)

Não precisa de CSS adicional - o seletor `.form-group input` já cobre `type="date"` e `type="file"`.

## Resultado

- Date picker abre calendário nativo
- File selector abre dialog de arquivo do SO
- Padding, bordas, estados de foco consistentes
