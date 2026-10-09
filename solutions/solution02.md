# Solução 2 - CSS Básico

## static/css/style.css (adições)

```css
.card {
	background: white;
	border-radius: var(--radius);
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
	padding: 1.5rem;
	margin-bottom: 1.5rem;
}
```

## index.html (main atualizado)

```html
<main>
	<div class="card">
		<h2>Bem-vindo</h2>
		<p>Esta é minha primeira página web.</p>
	</div>
	<div class="card">
		<h2>Funcionalidades</h2>
		<ul>
			<li>HTML Semântico</li>
			<li>Estrutura limpa</li>
			<li>Pronto para estilização</li>
		</ul>
	</div>
</main>
```

## Resultado

- Cards com fundo branco, bordas arredondadas, sombra sutil
- Espaçamento consistente entre cards
- Responsivo em todos tamanhos de tela
