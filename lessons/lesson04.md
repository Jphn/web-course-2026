# Aula 4 - Assets Estáticos e Dev Tools

## Objetivos

- Organizar arquivos estáticos (CSS, JS, imagens)
- Linkar assets corretamente no HTML
- Usar dev tools do navegador para debug

## Conteúdo (30 min)

1. **Estrutura da Pasta Static**:
    ```
    static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── images/
        └── logo.png
    ```
2. **Linkar Assets**: Caminhos relativos a partir do HTML
3. **Dev Tools do Navegador**:
    - Elements: inspecionar HTML/CSS
    - Console: erros JavaScript, `console.log`
    - Network: requisições/respostas, cache
    - Application: localStorage, cookies
4. **Cache Busting**: `style.css?v=1` ou hash no nome do arquivo

## Prática Guiada (40 min) - Code Along

```html
<!-- index.html (versão final com assets estáticos) -->
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Meu App</title>
		<link rel="stylesheet" href="static/css/style.css" />
		<link rel="icon" href="static/images/favicon.ico" />
	</head>
	<body>
		<header>
			<img
				src="static/images/logo.png"
				alt="Logo"
				width="32"
				height="32"
			/>
			<h1>Meu App</h1>
			<nav>
				<a href="index.html">Home</a>
				<a href="about.html">Sobre</a>
				<a href="contact.html">Contato</a>
			</nav>
		</header>

		<main>
			<div class="card">
				<h2>Bem-vindo</h2>
				<p>Assets estáticos carregados!</p>
				<button id="test-btn" class="btn">Testar JS</button>
			</div>
		</main>

		<footer><p>&copy; 2024 Meu App</p></footer>

		<script src="static/js/app.js"></script>
	</body>
</html>
```

```javascript
// static/js/app.js
console.log("App carregado");

document.getElementById("test-btn").addEventListener("click", () => {
	alert("JavaScript funciona!");
	console.log("Botão clicado");
});
```

```bash
# Criar placeholders
mkdir -p static/images
# Adicionar qualquer imagem pequena como logo.png
# Adicionar qualquer .ico como favicon.ico
```

## Exercício (10 min)

1. Abrir DevTools (F12), ir na aba **Network**, recarregar página
2. Observar requisições para: CSS, JS, imagem
3. Desabilitar cache, recarregar novamente
4. Verificar Console para mensagem "App carregado"
5. Adicionar `console.log('Exercício 4 completo')` ao `app.js`, verificar no Console

---

## Checklist

- [ ] Pasta `static/` organizada com css/, js/, images/
- [ ] Todos os assets carregam sem 404 (verificar aba Network)
- [ ] Favicon aparece na aba do navegador
- [ ] JavaScript executa (mensagem no console visível)
- [ ] Exercício: Exploração do DevTools completada
