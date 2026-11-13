# Aula 13 - Criar e listar itens

## Objetivos

- buscar registros no banco;
- inserir um registro;
- mostrar uma lista no template.

```python
def create_item(name, category, description):
    db = get_db()
    db.execute(
        "INSERT INTO items (name, category, description) VALUES (?, ?, ?)",
        (name, category, description),
    )
    db.commit()
```

Na rota, o GET mostra o formulário e o POST lê os campos, chama
`create_item()` e redireciona para a lista.
