# Aula 1 - HTML Básico

## Objetivos

- Entender fundamentos web: browser, server, papel do HTML
- Escrever estrutura HTML5 semântica
- Usar tags e atributos comuns corretamente

## Conteúdo (30 min)

1. **Como a Web Funciona**: Browser requisita → Server responde com HTML
2. **Estrutura de Arquivos**: `index.html` na raiz, pastas para organização
3. **Anatomia do HTML**: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
4. **Tags Semânticas**:
    - `<header>` - cabeçalho da página/seção
    - `<nav>` - links de navegação
    - `<main>` - conteúdo principal único
    - `<section>` - agrupamento temático
    - `<article>` - conteúdo autocontido
    - `<footer>` - rodapé da página/seção
5. **Tags Comuns**: `<h1>`-`<h6>`, `<p>`, `<a>`, `<ul>`/`<ol>`/`<li>`, `<img>`, `<div>`, `<span>`
6. **Atributos**: `id`, `class`, `href`, `src`, `alt`, `lang`

## Prática Guiada (40 min) - Code Along

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Meu App</title>
	</head>
	<body>
		<header>
			<h1>Meu App</h1>
			<nav>
				<a href="index.html">Home</a>
				<a href="about.html">Sobre</a>
				<a href="contact.html">Contato</a>
			</nav>
		</header>

		<main>
			<section>
				<h2>Bem-vindo</h2>
				<p>Esta é minha primeira página web.</p>
			</section>

			<section>
				<h2>Funcionalidades</h2>
				<ul>
					<li>HTML Semântico</li>
					<li>Estrutura limpa</li>
					<li>Pronto para estilização</li>
				</ul>
			</section>
		</main>

		<footer>
			<p>&copy; 2024 Meu App</p>
		</footer>
	</body>
</html>
```

## Exercício (10 min)

Criar `about.html` com:

- Mesmo header/nav/footer
- `<main>` com `<h2>Sobre</h2>` e parágrafo sobre você
- Link de volta para Home na nav

---

## Checklist

- [ ] `index.html` valida (W3C validator)
- [ ] Tags semânticas usadas corretamente
- [ ] Links da nav funcionam entre páginas
- [ ] Exercício: `about.html` criado e acessível
