# Aula 14 - Editar e excluir

## Objetivos

- carregar um item pelo seu `id`;
- reaproveitar o formulário para edição;
- excluir usando uma requisição POST.

Uma rota de edição combina duas ações:

```python
item = get_item(id)
if request.method == "GET":
    return render_template("items/form.html", item=item)

update_item(id, name, category, description)
return redirect(url_for("items"))
```

A exclusão usa POST porque altera dados. O botão de exclusão fica dentro de um
formulário próprio e pede confirmação no navegador.
