# Aula 15 - Polimento e Deploy

## Objetivos

- Adicionar páginas de erro (404, 500)
- Implementar logging
- Configurar variáveis de ambiente
- Rodar com servidor de produção (gunicorn)

## Conteúdo (30 min)

1. **Error Handlers**: `@app.errorhandler(404)`, `@app.errorhandler(500)`
2. **Logging**: `logging.basicConfig()`, logar erros e eventos importantes
3. **Variáveis de Ambiente**: `python-dotenv`, arquivo `.env`, `os.environ.get()`
4. **Servidor de Produção**: `gunicorn -w 4 run:app`
5. **Requirements**: `pip freeze > requirements.txt`

## Prática Guiada (40 min) - Code Along

```python
# app/__init__.py (completo com error handling)
import os
import logging
from flask import Flask, render_template, request
from .models import init_db, close_db

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    from .routes.main import main_bp
    from .routes.items import items_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp)

    # Template filter
    from datetime import datetime
    @app.template_filter('days_ago')
    def days_ago_filter(date_str):
        try:
            date = datetime.strptime(date_str[:10], '%Y-%m-%d').date()
            return (datetime.now().date() - date).days
        except:
            return '-'

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        logger.warning(f'404: {request.url}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        logger.error(f'500: {e}', exc_info=True)
        return render_template('errors/500.html'), 500

    return app
```

```html
<!-- templates/errors/404.html -->
{% extends 'base.html' %} {% block title %}Não Encontrado{% endblock %} {% block
content %}
<div class="error-page">
	<h1>404</h1>
	<p>Página não encontrada.</p>
	<a href="{{ url_for('main.index') }}" class="btn btn-primary"
		>Voltar ao Início</a
	>
</div>
{% endblock %}
```

```html
<!-- templates/errors/500.html -->
{% extends 'base.html' %} {% block title %}Erro Interno{% endblock %} {% block
content %}
<div class="error-page">
	<h1>500</h1>
	<p>Erro interno do servidor. Tente novamente mais tarde.</p>
	<a href="{{ url_for('main.index') }}" class="btn btn-primary"
		>Voltar ao Início</a
	>
</div>
{% endblock %}
```

```bash
# .env (criar na raiz do projeto, NÃO COMITAR)
SECRET_KEY=sua-chave-super-secreta-aqui
FLASK_ENV=development
DATABASE_URL=sqlite:///app.db
```

```python
# app/__init__.py (adicionar no topo)
from dotenv import load_dotenv
load_dotenv()
```

```bash
# Teste de produção
pip install gunicorn python-dotenv
pip freeze > requirements.txt

gunicorn -w 2 -b 127.0.0.1:8000 run:app
# Visitar http://127.0.0.1:8000
```

```css
/* Adicionar ao style.css */
.error-page {
	text-align: center;
	padding: 3rem;
}
.error-page h1 {
	font-size: 6rem;
	color: var(--secondary);
	margin-bottom: 1rem;
}
.error-page p {
	font-size: 1.25rem;
	color: var(--text-muted);
	margin-bottom: 2rem;
}
```

## Exercício (10 min)

Escolher UMA melhoria:

- [ ] Paginação (10 itens/página, `LIMIT/OFFSET`)
- [ ] Colunas ordenáveis (clicar header para ordenar)
- [ ] Filtro por categoria (dropdown)
- [ ] Contador de itens no badge da navbar

---

## Próximos Passos

| Tópico          | Por que                                |
| --------------- | -------------------------------------- |
| **Django**      | Framework completo, admin, ORM, auth   |
| **FastAPI**     | APIs modernas, async, docs automáticas |
| **Testes**      | `pytest`, `pytest-flask`, coverage     |
| **Deploy Real** | Docker, Nginx, PostgreSQL, CI/CD       |
| **Frontend**    | HTMX, Alpine.js, ou React/Vue          |

---

## Checklist Final

- [ ] App roda com `python run.py` (dev)
- [ ] App roda com `gunicorn run:app` (prod-like)
- [ ] `.env` configurado, `SECRET_KEY` segura
- [ ] `requirements.txt` atualizado
- [ ] Páginas 404/500 renderizam
- [ ] Logging aparece no console
- [ ] CRUD completo testado manualmente
- [ ] Código no GitHub com README
