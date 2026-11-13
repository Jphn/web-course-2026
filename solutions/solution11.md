# Solução 11 - Validação

A rota lê os campos com `request.form.get()`, verifica os valores permitidos,
usa `flash()` para informar o erro e retorna o mesmo template com os valores
preenchidos.
