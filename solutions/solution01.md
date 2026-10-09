# Solução 1 - HTML Básico

## about.html

```html
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Sobre</title>
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
				<h2>Sobre</h2>
				<p>
					Estou aprendendo desenvolvimento web com Python e Flask.
					Esta é minha primeira página HTML semântica.
				</p>
			</section>
		</main>

		<footer>
			<p>&copy; 2024 Meu App</p>
		</footer>
	</body>
</html>
```

## Pontos Principais

- Mesma estrutura do index.html
- Tags semânticas: header, nav, main, section, footer
- Links relativos funcionam entre arquivos
