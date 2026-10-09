# Exercício 2 - CSS Básico

## Objetivo

Adicionar componente `.card` e aplicá-lo.

## Instruções

1. No `static/css/style.css`, adicionar:

```css
.card {
	background: white;
	border-radius: var(--radius);
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
	padding: 1.5rem;
	margin-bottom: 1.5rem;
}
```

2. No `index.html`, envolver conteúdo principal:

```html
<main>
	<div class="card">
		<h2>Bem-vindo</h2>
		<p>Esta é minha primeira página web.</p>
	</div>
	<div class="card">
		<h2>Funcionalidades</h2>
		<ul>
			...
		</ul>
	</div>
</main>
```

## Teste

Recarregar página, verificar estilização do card.

## Critério de Sucesso

- Classe `.card` definida com propriedades especificadas
- Aplicada às seções de conteúdo
- Responsivo no mobile
