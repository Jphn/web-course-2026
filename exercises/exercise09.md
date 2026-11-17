# Exercício 9 - Navegação

## Objetivo

Adicionar páginas e navegação ao aplicativo Flask.

## Instruções

1. Crie `app/templates/about.html` e `app/templates/contact.html`.
2. Faça os dois templates estenderem `base.html`.
3. Adicione uma rota `/about` que renderize `about.html`.
4. Adicione uma rota `/contact` que renderize `contact.html`.
5. No menu de `app/templates/base.html`, use:

   ```html
   <a href="{{ url_for('about') }}">Sobre</a>
   <a href="{{ url_for('contact') }}">Contato</a>
   ```

6. Confirme que `/items/` continua renderizando
   `app/templates/items/list.html`.

## Critérios de sucesso

- `/about` e `/contact` funcionam;
- os templates reutilizam o layout base;
- os links são gerados com `url_for()`;
- não há caminhos HTML fixos para essas páginas.
