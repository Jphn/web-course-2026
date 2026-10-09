# Exercício 4 - Assets Estáticos e Dev Tools

## Objetivo

Explorar dev tools do navegador e verificar carregamento de assets.

## Instruções

1. Abrir `index.html` no browser
2. Abrir DevTools (F12)
3. Ir na aba **Network**, recarregar página
4. Observar requisições para:
    - `style.css`
    - `app.js`
    - `logo.png`
    - `favicon.ico`
5. Clicar cada requisição, verificar aba **Headers** para status 200
6. Ir na aba **Console**, verificar mensagem "App carregado"
7. Adicionar `console.log('Exercício 4 completo')` ao `app.js`, recarregar

## Teste

Todos assets carregam com status 200, console mostra mensagens.

## Critério de Sucesso

- Aba Network mostra todos assets estáticos
- Nenhum erro 404
- Logs do console visíveis
