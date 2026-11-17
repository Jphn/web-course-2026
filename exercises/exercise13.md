# Exercício 13 - Criar e listar

## Objetivo

Conectar o formulário de novo item ao SQLite e mostrar os registros salvos.

## Instruções

1. Em `app/models.py`, implemente `list_items()` com um `SELECT`.
2. Implemente `create_item(name, category, description)` com um `INSERT`
   parametrizado e `commit()`.
3. Em `app/routes.py`, faça `/items/` chamar `list_items()` e passar o
   resultado para `items/list.html`.
4. Faça `/items/new` aceitar GET e POST.
5. No POST, leia `name`, `category` e `description`, chame `create_item()` e
   redirecione para `items`.
6. Em `app/templates/items/list.html`, percorra `items` e mostre nome,
   categoria e descrição.

## Critérios de sucesso

- o formulário de novo item aparece;
- um item válido é salvo no SQLite;
- o item aparece na lista após o redirecionamento;
- os valores são enviados ao SQL por parâmetros;
- a lista informa quando não há itens.
