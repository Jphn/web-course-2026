# Exercício 6 - Herança de templates

## Objetivo

Criar uma página de serviços usando o layout base, sem repetir o cabeçalho e o
rodapé.

## Instruções

1. Crie `templates/services.html` usando `extends`, `title` e `content`.
2. No menu do `base.html`, adicione um link HTML simples:

```html
<!-- templates/base.html -->
<a href="services.html">Serviços</a>
```

3. Renderize o template com o mesmo mecanismo usado na Aula 5.

`url_for()` será apresentado depois que Flask for introduzido.

## Critério de sucesso

- A página estende `base.html`.
- O conteúdo específico aparece no bloco `content`.
- O cabeçalho e o rodapé aparecem uma única vez.
