# Aula 15 - Revisão e apresentação

## Objetivos

- revisar o caminho completo dos dados;
- testar o fluxo CRUD;
- explicar a organização do projeto;
- apresentar uma aplicação funcional.

## Revisão do fluxo

Quando uma pessoa cria um item:

1. o formulário HTML envia os campos por POST;
2. a rota lê e valida os valores;
3. a função do modelo executa o SQL parametrizado;
4. o SQLite salva o registro;
5. a rota redireciona para a lista;
6. o template mostra os dados salvos.

O mesmo caminho é usado para editar e excluir, com a diferença de que essas
operações também recebem o `id` do item.

## Exercício (20 min)

Revise o projeto e prepare uma demonstração de cinco minutos. Siga esta ordem:

1. abra a página inicial e mostre a navegação;
2. crie um item válido;
3. tente enviar um formulário inválido e mostre a mensagem;
4. edite o item criado;
5. exclua o item;
6. explique a função de `routes.py`, `models.py`, templates e banco SQLite.

## Checklist do projeto

- [ ] O servidor inicia com `python run.py`
- [ ] A página inicial possui navegação
- [ ] O formulário valida nome e categoria
- [ ] A lista lê dados do SQLite
- [ ] É possível criar, editar e excluir um item
- [ ] Os links usam `url_for`
- [ ] Os textos visíveis estão em pt-BR
- [ ] O código está organizado em `routes.py` e `models.py`

Como próximos passos, o professor pode apresentar autenticação, testes,
paginação e deploy sem exigir esses assuntos no projeto inicial.
