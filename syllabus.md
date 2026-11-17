# Ementa - Desenvolvimento Web Básico com Python

**Carga horária:** 30h (15 aulas × 2h)
**Público:** iniciantes em desenvolvimento web
**Pré-requisito:** noções de variáveis, condicionais, loops e funções em Python

## Módulo 1: páginas web (aulas 1-4)

HTML, semântica, CSS, box model, flexbox, formulários e arquivos estáticos.

## Módulo 2: templates (aulas 5-7)

Variáveis, condicionais, loops, herança de templates, includes e macros
simples.

## Módulo 3: Flask (aulas 8-11)

Instalação, primeira aplicação, rotas, `url_for`, GET, POST, redirect,
formulários e mensagens flash.

## Módulo 4: banco e CRUD (aulas 12-15)

SQLite, consultas parametrizadas, conexão por requisição, criação, listagem,
edição, exclusão e revisão do projeto.

## Resultado esperado

Ao final, o aluno consegue criar uma aplicação Flask pequena, organizar seus
arquivos, receber dados de um formulário e persistir esses dados em SQLite.

## Ordem das dependências

Cada etapa usa apenas conceitos apresentados anteriormente:

| Conceito | Primeira aula |
| --- | --- |
| Classes `.card`, `.form-group` e `.btn` | 2 e 3 |
| Includes e macros | 7 |
| Classes `.badge-*` | 7 |
| Flask e `render_template` | 8 |
| `url_for` e rotas com nome | 9 |
| `items/list.html` | 9 |
| `request.form` e redirecionamento | 10 |
| `flash()` e classes `.flash-*` | 11 |
| `items/form.html` | 11 |
| SQLite, `g` e `current_app` | 12 |
| CRUD de itens | 13 e 14 |

Quando um exemplo usa uma classe CSS ou função nova, a aula correspondente
também apresenta sua definição ou indica explicitamente onde ela foi criada.

Autenticação, CSRF, autorização, deploy, testes automatizados, paginação e
logging ficam como próximos cursos, não como requisito desta introdução.
