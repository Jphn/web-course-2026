# Projeto inicial

Aplicação simples usada durante o curso para aprender Flask. O aluno
constrói um pequeno cadastro de itens com HTML, formulários e SQLite.

## Executar

```bash
cd project_starter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Acesse <http://localhost:5000>. O banco `app/app.db` é criado
automaticamente e já está no `.gitignore`.

## Rotas

| Rota | Finalidade |
| --- | --- |
| `/` | Página inicial |
| `/about` | Página sobre |
| `/contact` | Página de contato |
| `/items/` | Lista de itens |
| `/items/new` | Criação de item |
| `/items/<id>/edit` | Edição de item |
| `/items/<id>/delete` | Exclusão via `POST` |
