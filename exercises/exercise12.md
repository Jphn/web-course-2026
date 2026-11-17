# Exercício 12 - Criar a tabela

Configure o banco SQLite da aplicação e crie a tabela `items`.

## Instruções

1. Em `create_app()`, configure:

   ```python
   app.config["DATABASE"] = os.path.join(app.root_path, "app.db")
   ```

2. Crie `app/models.py`.
3. Implemente `get_db()` usando `g` e `sqlite3.Row`.
4. Implemente `close_db()` para fechar a conexão ao final da requisição.
5. Implemente `init_db()` com a tabela `items` e as colunas:
   `id`, `name`, `category`, `description` e `created_at`.
6. Chame `init_db()` dentro de `app.app_context()` em `create_app()`.
7. Registre `close_db()` com `app.teardown_appcontext()`.
8. Inicie a aplicação e confirme que `app/app.db` foi criado.

## Critérios de sucesso

- a aplicação inicia sem erro;
- o arquivo `app.db` aparece dentro da pasta `app`;
- a tabela `items` é criada automaticamente;
- a conexão é fechada ao final da requisição;
- executar a aplicação novamente não apaga os dados existentes.
