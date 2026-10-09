# Solução 4 - Assets Estáticos e Dev Tools

## Passos de Exploração do DevTools

1. **Aba Network** (após recarregar):

    ```
    Name          Status  Type        Size    Time
    index.html    200     document    2.1 KB  15ms
    style.css     200     stylesheet  1.2 KB  8ms
    app.js        200     script      0.3 KB  5ms
    logo.png      200     image       2.4 KB  12ms
    favicon.ico   200     image       1.1 KB  6ms
    ```

2. **Headers** (clicar style.css):
    - Request URL: `http://localhost:5000/static/css/style.css`
    - Status Code: 200 OK
    - Content-Type: text/css

3. **Console**:
    ```
    App carregado
    Exercício 4 completo
    ```

## Checklist de Verificação

- [ ] Todas 5 requisições retornam 200
- [ ] Nenhuma requisição vermelha (falhou)
- [ ] Console mostra ambas mensagens de log
- [ ] Cache desabilitado mostra requisições frescas no recarregar
