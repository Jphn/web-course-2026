# Exercício 8 - Primeira rota Flask

## Objetivo

Criar uma aplicação Flask pequena, iniciar o servidor e adicionar uma segunda
rota. A rota `/` será a página inicial e `/hello` mostrará uma mensagem em
HTML.

## Preparação

Na pasta do exercício, crie e ative um ambiente virtual:

```bash
# terminal
python -m venv .venv
```

Linux/macOS:

```bash
# terminal
source .venv/bin/activate
```

Windows:

```powershell
# terminal
.venv\Scripts\activate
```

Instale o Flask:

```bash
# terminal
pip install Flask
```

## Instruções

1. Crie a pasta `app`.
2. Crie `app/__init__.py` com uma função `create_app()` que:
   - crie uma aplicação com `Flask(__name__)`;
   - registre uma rota `/` que retorne `"Olá, Flask!"`;
   - retorne a aplicação.
3. Crie `run.py` para chamar `create_app()` e iniciar o servidor com
   `app.run(debug=True)`.
4. Em `app/__init__.py`, adicione uma rota `/hello` que retorne o seguinte
   HTML:

   ```html
   <h1>Olá, estudante!</h1>
   <p>Esta é minha primeira rota Flask.</p>
   ```

5. Inicie a aplicação:

   ```bash
   python run.py
   ```

6. Abra no navegador:
   - `http://127.0.0.1:5000/`
   - `http://127.0.0.1:5000/hello`

Para encerrar o servidor, pressione `Ctrl+C` no terminal.

## Critérios de sucesso

- o servidor inicia sem erro;
- `/` continua mostrando a mensagem inicial;
- `/hello` mostra o título e o parágrafo solicitados;
- as duas rotas estão registradas na aplicação retornada por `create_app()`;
- a aplicação não cria um segundo objeto `Flask`.
