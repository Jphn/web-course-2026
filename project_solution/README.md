# Projeto final

Referência do projeto construído durante o curso: um cadastro de itens com
Flask, formulários, templates e SQLite.

## Executar

```bash
cd project_solution
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Acesse <http://localhost:5000>. O banco `app/app.db` é criado
automaticamente e já está no `.gitignore`.

## O que foi praticado

- páginas HTML com templates Jinja;
- formulários GET e POST;
- validação simples no servidor;
- criação, listagem, edição e exclusão;
- armazenamento em SQLite;
- organização do código em `routes.py` e `models.py`.

Os textos exibidos estão em pt-BR. Nomes de variáveis, arquivos e pastas
continuam em inglês para manter as convenções do código.
