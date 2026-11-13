# Aula 10 - Formulários, GET e POST

## Objetivos

- diferenciar GET e POST;
- ler dados enviados por um formulário;
- redirecionar depois de salvar.

```python
from flask import redirect, request, url_for

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        return redirect(url_for("hello"))
    return render_template("hello.html")
```

O padrão de redirecionar depois de um POST evita o reenvio acidental do
formulário ao atualizar a página.
