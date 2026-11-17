# Exercício 14 - CRUD completo

## Objetivo

Adicionar edição e exclusão ao cadastro de itens.

## Instruções

1. Em `app/models.py`, implemente `get_item()`, `update_item()` e
   `delete_item()`.
2. Crie `/items/<int:id>/edit` com GET e POST.
3. No GET, reutilize `items/form.html` preenchendo os valores atuais.
4. No POST, atualize o item e redirecione para `items`.
5. Crie `/items/<int:id>/delete` aceitando somente POST.
6. Adicione à lista um link de edição e um formulário separado para exclusão.
7. Retorne 404 quando o `id` não existir.

## Critérios de sucesso

- um item pode ser editado;
- um item pode ser excluído;
- excluir exige POST;
- registros inexistentes retornam 404;
- a lista mostra os dados atualizados.
