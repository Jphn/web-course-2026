# Aula 3 - Formulários HTML

## Objetivos

- Construir formulários HTML acessíveis
- Usar tipos de input apropriados
- Aplicar atributos de validação nativos

## Conteúdo (30 min)

1. **Elemento Form**: `<form method="POST" action="/submit">`
2. **Tipos de Input**:
    - `text` - linha única
    - `email` - validação de email
    - `number` - apenas números
    - `textarea` - multi-linha
    - `select` + `option` - dropdown
    - `checkbox` - múltipla escolha
    - `radio` - escolha única
3. **Labels**: `<label for="id">` vinculado a `<input id="id">`
4. **Atributos de Validação**: `required`, `minlength`, `maxlength`, `min`, `max`, `pattern`
5. **Acessibilidade**: `aria-describedby`, `fieldset`/`legend` para grupos

## Prática Guiada (40 min) - Code Along

```html
<!-- form.html (autônomo para prática) -->
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Prática de Formulário</title>
		<link rel="stylesheet" href="static/css/style.css" />
	</head>
	<body>
		<header>
			<h1>Meu App</h1>
			<nav><a href="index.html">Home</a></nav>
		</header>

		<main>
			<form class="form" method="POST" action="/items">
				<div class="form-group">
					<label for="name">Nome *</label>
					<input
						type="text"
						id="name"
						name="name"
						required
						maxlength="100"
					/>
				</div>

				<div class="form-group">
					<label for="email">Email</label>
					<input type="email" id="email" name="email" />
				</div>

				<div class="form-group">
					<label for="quantity">Quantidade</label>
					<input
						type="number"
						id="quantity"
						name="quantity"
						min="1"
						max="100"
					/>
				</div>

				<div class="form-group">
					<label for="description">Descrição</label>
					<textarea
						id="description"
						name="description"
						rows="4"
					></textarea>
				</div>

				<div class="form-group">
					<label for="category">Categoria *</label>
					<select id="category" name="category" required>
						<option value="">Selecione...</option>
						<option value="work">Trabalho</option>
						<option value="personal">Pessoal</option>
						<option value="study">Estudo</option>
					</select>
				</div>

				<fieldset class="form-group">
					<legend>Opções</legend>
					<label
						><input type="checkbox" name="notify" value="email" />
						Notificações por email</label
					>
					<label
						><input type="checkbox" name="notify" value="push" />
						Notificações push</label
					>
				</fieldset>

				<fieldset class="form-group">
					<legend>Prioridade</legend>
					<label
						><input type="radio" name="priority" value="low" />
						Baixa</label
					>
					<label
						><input
							type="radio"
							name="priority"
							value="medium"
							checked
						/>
						Média</label
					>
					<label
						><input type="radio" name="priority" value="high" />
						Alta</label
					>
				</fieldset>

				<button type="submit" class="btn">Enviar</button>
			</form>
		</main>

		<footer><p>&copy; 2024 Meu App</p></footer>
	</body>
</html>
```

```css
/* Adicionar ao style.css */
.form {
	background: white;
	padding: 1.5rem;
	border-radius: var(--radius);
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
	max-width: 600px;
	margin: 0 auto;
}
.form-group {
	margin-bottom: 1rem;
}
.form-group label {
	display: block;
	margin-bottom: 0.5rem;
	font-weight: 600;
}
.form-group input,
.form-group textarea,
.form-group select {
	width: 100%;
	padding: 0.75rem;
	border: 1px solid #ddd;
	border-radius: 4px;
	font-size: 1rem;
	font-family: inherit;
}
.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
	outline: none;
	border-color: var(--secondary);
	box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
}
.form-group fieldset {
	border: 1px solid #ddd;
	border-radius: 4px;
	padding: 1rem;
}
.form-group legend {
	font-weight: 600;
	padding: 0 0.5rem;
}
.btn {
	background: var(--secondary);
	color: white;
	border: none;
	padding: 0.75rem 1.5rem;
	border-radius: 4px;
	cursor: pointer;
	font-size: 1rem;
}
.btn:hover {
	background: #2980b9;
}
```

## Exercício (10 min)

Adicionar ao formulário:

- Input de data (`type="date"`) para "Data de Vencimento"
- Input de arquivo (`type="file"`) para "Anexo"
- Estilizá-los consistentemente

---

## Checklist

- [ ] Todos os tipos de input renderizam corretamente
- [ ] Labels vinculados via `for`/`id`
- [ ] Atributos de validação funcionam (tentar enviar vazio)
- [ ] Checkboxes e radios agrupados com fieldset
- [ ] Exercício: inputs de data e arquivo adicionados
