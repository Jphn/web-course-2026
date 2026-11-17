# Exercício 10 - Formulário de contato

Substitua a página estática `/contact` criada na Aula 9 por um formulário de
contato. Depois do envio, mostre uma confirmação usando o nome e a mensagem
recebidos.

Não monte HTML concatenando strings em Python. Use um template.

## Instruções

1. Importe `redirect`, `render_template`, `request` e `url_for`.
2. Altere a rota existente `/contact` para aceitar `GET` e `POST`.
3. Crie um formulário com os campos `name` e `message`.
4. Em um POST, leia e remova espaços dos valores enviados:

   ```python
   name = request.form.get("name", "").strip()
   message = request.form.get("message", "").strip()
   ```

5. Redirecione para a própria rota com `name` e `message` na query string:

   ```python
   return redirect(url_for("contact", name=name, message=message))
   ```

6. Em um GET, renderize `contact.html` passando os valores da query string.
7. Crie `templates/contact.html` com um formulário `method="post"` e mostre
   uma confirmação somente quando houver uma mensagem:

   ```html
   {% if message %}
       <p>Obrigado, {{ name }}. Recebemos sua mensagem:</p>
       <p>{{ message }}</p>
   {% endif %}
   ```

## Critérios de sucesso

- o formulário aparece ao acessar `/contact`;
- o nome é enviado por POST;
- a mensagem é enviada por POST;
- a página mostra a confirmação após o envio;
- atualizar a página não reenvia o formulário;
- o HTML fica no template, não em uma string Python.
