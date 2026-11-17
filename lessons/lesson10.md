# Aula 10 - Formulários, GET e POST

## Pré-requisito

A aplicação já possui rotas, templates e links gerados com `url_for()`.

## Objetivos

- diferenciar GET e POST;
- ler dados enviados por um formulário;
- redirecionar depois de salvar.

```python
# app/routes.py
from flask import redirect, render_template, request, url_for

def register_routes(app):
    @app.route("/hello", methods=["GET", "POST"])
    def hello():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            return redirect(url_for("hello", name=name))
        return render_template("hello.html", name=request.args.get("name", ""))
```

O padrão de redirecionar depois de um POST evita o reenvio acidental do
formulário ao atualizar a página.

Crie o template `app/templates/hello.html`:

```html
<!-- templates/hello.html -->
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Olá</title>
</head>
<body>
    <h1>Formulário</h1>

    <form method="post">
        <label for="name">Nome</label>
        <input type="text" id="name" name="name" value="{{ name }}">
        <button type="submit">Enviar</button>
    </form>

    {% if name %}
        <p>Olá, {{ name }}!</p>
    {% endif %}
</body>
</html>
```

A rota exibe o formulário em um acesso GET. Depois do POST, ela redireciona
para a própria rota com o nome na query string, e o template mostra a
saudação.

## Exercício (10 min)

Crie `app/templates/hello.html` e conecte-o à rota `/hello`:

1. adicione um campo de texto com `name="name"`;
2. envie o formulário com o método `POST`;
3. mostre `Olá, nome!` somente quando um nome tiver sido informado;
4. mantenha o nome preenchido no campo depois do envio;
5. teste a rota acessando `/hello` e enviando o formulário.

## Checklist

- [ ] O template está em `app/templates/hello.html`
- [ ] O formulário usa `method="post"`
- [ ] A rota lê o valor com `request.form`
- [ ] O nome aparece na saudação
- [ ] O POST redireciona antes de mostrar o resultado
