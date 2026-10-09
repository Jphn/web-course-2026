# Aula 8 - Flask Básico

## Objetivos

- Configurar ambiente virtual Python
- Criar app Flask com factory pattern
- Conectar templates às rotas

## Conteúdo (30 min)

1. **Virtual Environment**: `python -m venv venv`, ativar, `pip install flask`
2. **Estrutura do Projeto**:
    ```
    project/
    ├── run.py
    ├── requirements.txt
    └── app/
        ├── __init__.py
        ├── routes/
        └── templates/
    ```
3. **App Factory**: Função `create_app()` retorna instância Flask configurada
4. **Rotas**: Decorador `@app.route('/')`, função retorna `render_template()`
5. **Debug Mode**: `app.run(debug=True)` para auto-reload e páginas de erro

## Prática Guiada (40 min) - Code Along

```python
# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'dev-secret-change-in-production'

    # Registrar rotas
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
```

```python
# app/routes/main.py
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
```

```bash
# Setup
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install flask
pip freeze > requirements.txt

# Rodar
python run.py
# Visitar http://localhost:5000
```

## Exercício (10 min)

1. Adicionar rota `/hello/<name>` no `main.py`
2. Criar `templates/hello.html` estendendo base
3. Exibir "Hello, {name}!" no block content
4. Testar: visitar `/hello/World`

---

## Checklist

- [ ] Virtual environment criado e ativado
- [ ] Flask instalado, `requirements.txt` gerado
- [ ] `run.py` inicia servidor na porta 5000
- [ ] Factory pattern no `app/__init__.py`
- [ ] Blueprints registrados
- [ ] Todos templates anteriores renderizam corretamente
- [ ] Exercício: rota `/hello/<name>` funciona
