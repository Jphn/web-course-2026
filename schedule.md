# Cronograma Detalhado - 15 Aulas × 2h

## Formato de cada aula (120 min)

| Tempo       | Atividade                         |
| ----------- | --------------------------------- |
| 0-10 min    | Revisão / aquecimento             |
| 10-50 min   | Conteúdo novo + demo ao vivo      |
| 50-55 min   | Pausa                             |
| 55-105 min  | Prática guiada (code along)       |
| 105-115 min | Exercício individual              |
| 115-120 min | Dúvidas + preview da próxima aula |

---

## Detalhamento por Aula

### Aula 1 - HTML Básico (2h)

- **10 min:** Fundamentos web, browser vs server, estrutura de arquivos
- **30 min:** Tags semânticas (header, nav, main, section, article, footer), atributos, aninhamento
- **5 min:** Pausa
- **40 min:** Code along: `index.html` com estrutura semântica completa
- **10 min:** Exercício: Criar `about.html` com mesma estrutura
- **5 min:** Dúvidas + preview Aula 2

### Aula 2 - CSS Básico (2h)

- **10 min:** Revisão: estrutura HTML
- **30 min:** Box model, flexbox, variáveis CSS, `@media` responsivo, mobile-first
- **5 min:** Pausa
- **40 min:** Code along: `style.css` com navbar, cards, footer, layout responsivo
- **10 min:** Exercício: Adicionar efeitos hover e nova variável de cor
- **5 min:** Dúvidas + preview Aula 3

### Aula 3 - Formulários HTML (2h)

- **10 min:** Revisão: layout CSS
- **30 min:** Elemento form, tipos de input (text, email, number, textarea, select), labels, atributos de validação, acessibilidade
- **5 min:** Pausa
- **40 min:** Code along: Formulário completo com todos os tipos de input, estilizado com CSS
- **10 min:** Exercício: Adicionar grupo de checkboxes e radio buttons
- **5 min:** Dúvidas + preview Aula 4

### Aula 4 - Assets Estáticos (2h)

- **10 min:** Revisão: Formulários
- **30 min:** Linkar CSS, organizar pasta `static/`, dev tools do navegador (inspecionar, network, console)
- **5 min:** Pausa
- **40 min:** Code along: Refatorar para `static/css/style.css`, adicionar placeholder `static/js/`, usar dev tools
- **10 min:** Exercício: Adicionar favicon e testar comportamento de cache
- **5 min:** Dúvidas + preview Aula 5

### Aula 5 - Jinja2 Básico (2h)

- **10 min:** Revisão: Assets estáticos, por que templates?
- **30 min:** `{{ variavel }}`, `{% if %}`, `{% for %}`, `{% endif %}`, `{% endfor %}`, renderização via Python
- **5 min:** Pausa
- **40 min:** Code along: Script Python renderizando templates com variáveis, loops, condicionais
- **10 min:** Exercício: Criar template mostrando lista com mensagem condicional "vazio"
- **5 min:** Dúvidas + preview Aula 6

### Aula 6 - Herança de Templates (2h)

- **10 min:** Revisão: Sintaxe Jinja2
- **30 min:** `base.html` com `{% block %}`, `{% extends %}`, `{% block.super %}`, princípio DRY
- **5 min:** Pausa
- **40 min:** Code along: Layout base com header, footer, bloco de conteúdo; páginas filhas (home, about, contact)
- **10 min:** Exercício: Criar `services.html` estendendo base com conteúdo único
- **5 min:** Dúvidas + preview Aula 7

### Aula 7 - Partials de Templates (2h)

- **10 min:** Revisão: Herança
- **30 min:** `{% include %}`, `{% macro %}`, componentes reutilizáveis (navbar, card, flash messages)
- **5 min:** Pausa
- **40 min:** Code along: Extrair navbar, card, macros de flash; usar em todos os templates
- **10 min:** Exercício: Criar macro de `pagination`
- **5 min:** Dúvidas + preview Aula 8

### Aula 8 - Flask Básico (2h)

- **10 min:** Revisão: Templates, por que backend?
- **30 min:** Python venv, `pip install flask`, app factory, `@app.route`, `render_template`, `app.run(debug=True)`
- **5 min:** Pausa
- **40 min:** Code along: `run.py`, `app/__init__.py`, conectar Flask aos templates existentes
- **10 min:** Exercício: Adicionar rota `/hello/<name>` renderizando template com nome
- **5 min:** Dúvidas + preview Aula 9

### Aula 9 - Rotas e Métodos HTTP (2h)

- **10 min:** Revisão: Flask básico
- **30 min:** GET vs POST, `methods=['GET','POST']`, `request.method`, `redirect`, `url_for`, padrão PRG
- **5 min:** Pausa
- **40 min:** Code along: Rota `/items` lidando com GET (listar) e POST (criar), redirect após POST
- **10 min:** Exercício: Criar `/greet/<name>` com GET (mostrar) e POST (redirect para GET)
- **5 min:** Dúvidas + preview Aula 10

### Aula 10 - Tratamento de Formulários (2h)

- **10 min:** Revisão: Métodos HTTP
- **30 min:** `request.form.get()`, validação server-side, `flash()` messages, categorias, repopular formulários
- **5 min:** Pausa
- **40 min:** Code along: Formulário de criação de item com validação, flash success/error, feedback estilizado
- **10 min:** Exercício: Adicionar campo "category" select com validação
- **5 min:** Dúvidas + preview Aula 11

### Aula 11 - Blueprints e Estrutura (2h)

- **10 min:** Revisão: Formulários, complexidade crescente
- **30 min:** `Blueprint`, `app.register_blueprint()`, `url_prefix`, rotas modulares, app factory pattern
- **5 min:** Pausa
- **40 min:** Code along: Separar rotas em `main.py` e `items.py`, registrar blueprints, atualizar `url_for`
- **10 min:** Exercício: Criar blueprint `auth.py` placeholder para futuro
- **5 min:** Dúvidas + preview Aula 12

### Aula 12 - SQLite e Models (2h)

- **10 min:** Revisão: Blueprints
- **30 min:** Módulo `sqlite3`, conexão por request (`g`), `row_factory`, `CREATE TABLE`, funções CRUD em `models.py`
- **5 min:** Pausa
- **40 min:** Code along: `models.py` com `get_db`, `init_db`, `list_items`, `get_item`, `create_item`, `update_item`, `delete_item`
- **10 min:** Exercício: Adicionar função `count_items()`
- **5 min:** Dúvidas + preview Aula 13

### Aula 13 - Listagem e Criação (2h)

- **10 min:** Revisão: Models
- **30 min:** Renderizar tabela com `{% for %}`, links de ação com `url_for`, rota de criação (GET form, POST salvar), flash feedback
- **5 min:** Pausa
- **40 min:** Code along: `/items` página de lista com tabela, `/items/new` formulário de criação, validação, redirect
- **10 min:** Exercício: Adicionar coluna "created_at" formatada no template
- **5 min:** Dúvidas + preview Aula 14

### Aula 14 - Edição e Exclusão (2h)

- **10 min:** Revisão: Listagem e Criação
- **30 min:** Rota de edição (GET pré-preenche, POST atualiza), Rota de exclusão (apenas POST, confirmação), práticas de segurança
- **5 min:** Pausa
- **40 min:** Code along: `/items/<id>/edit` e `/items/<id>/delete` totalmente funcionais
- **10 min:** Exercício: Adicionar botão "Cancelar" no form de edição linkando para lista
- **5 min:** Dúvidas + preview Aula 15

### Aula 15 - Polimento e Deploy (2h)

- **10 min:** Revisão: CRUD completo
- **30 min:** Error handlers (404, 500), logging, `python-dotenv`, `.env`, `gunicorn`, `requirements.txt`
- **5 min:** Pausa
- **40 min:** Code along: Adicionar páginas 404/500, logging, config de env, testar com gunicorn
- **10 min:** Exercício: Adicionar busca/filtro na lista (bônus opcional)
- **5 min:** Encerramento: Certificados, próximos passos (Django, FastAPI, React, testes, CI/CD)

---

## Entregas dos Alunos

| Aula  | Entrega                                       |
| ----- | --------------------------------------------- |
| 1-4   | Arquivos de exercício em pasta local / GitHub |
| 5-7   | Arquivos de template + screenshots            |
| 8-11  | App Flask com rotas + repositório GitHub      |
| 12-14 | CRUD funcional + banco de dados               |
| 15    | Projeto completo no GitHub com README         |
