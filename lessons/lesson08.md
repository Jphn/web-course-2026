# Aula 8 - Primeiro aplicativo Flask

## Objetivos

- instalar Flask em um ambiente virtual;
- criar a aplicação e iniciar o servidor;
- entender a relação entre Python, rota e navegador.

## Código inicial

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Olá, Flask!"

    return app
```

```python
# run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

`debug=True` ajuda durante a aula e não deve ser usado como configuração de
produção.

## Exercício (10 min)

Modifique a aplicação para criar uma segunda rota:

1. mantenha a rota `/` mostrando `Olá, Flask!`;
2. crie a rota `/hello` no mesmo `create_app()`;
3. faça `/hello` retornar este conteúdo HTML:

```html
<!-- app/__init__.py: conteúdo retornado pela rota /hello -->
   <h1>Olá, estudante!</h1>
   <p>Esta é minha primeira rota Flask.</p>
```

## Checklist

- [ ] O Flask foi instalado em um ambiente virtual
- [ ] A aplicação inicia com `python run.py`
- [ ] A rota `/` continua funcionando
- [ ] A rota `/hello` mostra o título e o parágrafo solicitados
- [ ] Existe apenas um objeto `Flask`, criado por `create_app()`
