# Aula 2 - CSS Básico

## Objetivos

- Estilizar HTML com CSS: box model, flexbox, variáveis
- Criar layouts responsivos (mobile-first)
- Organizar CSS em arquivo externo

## Conteúdo (30 min)

1. **CSS Básico**: Seletores (tag, `.class`, `#id`), propriedades, valores
2. **Box Model**: `margin`, `border`, `padding`, `box-sizing: border-box`
3. **Flexbox**: `display: flex`, `gap`, `justify-content`, `align-items`, `flex-wrap`
4. **Variáveis CSS**: `:root { --cor: valor; }`, `var(--cor)`
5. **Design Responsivo**: Mobile-first, `@media (min-width: 768px)`
6. **CSS Externo**: `<link rel="stylesheet" href="static/css/style.css">`

## Prática Guiada (40 min) - Code Along

```css
/* static/css/style.css */
:root {
	--primary: #2c3e50;
	--secondary: #3498db;
	--bg: #f8f9fa;
	--text: #333;
	--spacing: 1rem;
	--radius: 8px;
}

* {
	box-sizing: border-box;
	margin: 0;
	padding: 0;
}

body {
	font-family: system-ui, sans-serif;
	background: var(--bg);
	color: var(--text);
	line-height: 1.6;
	min-height: 100vh;
	display: flex;
	flex-direction: column;
}

header {
	background: var(--primary);
	color: white;
	padding: var(--spacing);
	display: flex;
	justify-content: space-between;
	align-items: center;
	flex-wrap: wrap;
	gap: var(--spacing);
}

header nav a {
	color: white;
	text-decoration: none;
	margin-left: var(--spacing);
}
header nav a:hover {
	text-decoration: underline;
}

main {
	flex: 1;
	max-width: 800px;
	margin: 2rem auto;
	padding: var(--spacing);
	width: 100%;
}

footer {
	text-align: center;
	padding: 2rem;
	color: #666;
	border-top: 1px solid #ddd;
	margin-top: auto;
}

/* Mobile-first: estilos base acima */
@media (min-width: 768px) {
	header {
		padding: var(--spacing) 2rem;
	}
	main {
		padding: 2rem;
	}
}
```

```html
<!-- index.html (head atualizado) -->
<head>
	...
	<link rel="stylesheet" href="static/css/style.css" />
</head>
```

## Exercício (10 min)

Adicionar ao `style.css`:

- Classe `.card`: fundo branco, bordas arredondadas, sombra sutil, padding
- Aplicar em `<div class="card">` envolvendo conteúdo principal no `index.html`

---

## Checklist

- [ ] `style.css` linkado no HTML
- [ ] Flexbox na navbar funciona
- [ ] Variáveis CSS definidas e usadas
- [ ] Responsivo no breakpoint 768px
- [ ] Exercício: `.card` criado e aplicado
