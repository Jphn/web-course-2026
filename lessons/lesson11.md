# Aula 11 - Validação e mensagens

## Objetivos

- validar dados no servidor;
- mostrar uma mensagem para a pessoa usuária;
- manter os valores preenchidos quando houver erro.

```python
from flask import flash

name = request.form.get("name", "").strip()
if not name:
    flash("O nome é obrigatório.", "error")
    return render_template("items/form.html", name=name), 400

flash("Item criado com sucesso!", "success")
return redirect(url_for("items"))
```

O navegador pode validar um formulário, mas a aplicação também precisa validar
os dados recebidos no servidor.
