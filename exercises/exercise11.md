# Exercício 11 - Validar um formulário

## Objetivo

Validar os dados do formulário no servidor e informar erros com mensagens
flash.

## Instruções

1. Em `app/__init__.py`, configure `SECRET_KEY` antes de usar `flash()`:

   ```python
   # app/__init__.py
   app.config["SECRET_KEY"] = "dev-secret"
   ```

2. Na rota que recebe o formulário, leia `name`, `category` e `description`
   com `request.form.get(...).strip()`.
3. Rejeite os seguintes casos:
   - nome vazio;
   - categoria vazia;
   - categoria diferente de `work`, `personal` ou `study`.
4. Use `flash()` com mensagens em pt-BR.
5. Em caso de erro, renderize `items/form.html` novamente e passe os valores
   recebidos.
6. Inclua a macro de mensagens flash no layout base e confirme que as classes
   `.flash-success` e `.flash-error` estão estilizadas.

## Critérios de sucesso

- dados inválidos não são salvos;
- a mensagem de erro aparece na página;
- os valores digitados permanecem no formulário;
- uma categoria válida pode continuar para o próximo passo;
- mensagens flash usam classes CSS visíveis.
