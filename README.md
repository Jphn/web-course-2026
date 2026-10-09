# Desenvolvimento Web Básico com Python

Curso de 30 horas (15 aulas × 2h) para iniciantes absolutos.

## Stack

- **Python 3.10+**
- **Flask** - microframework web
- **Jinja2** - template engine (já incluso no Flask)
- **HTML/CSS** - frontend básico
- **SQLite** - banco de dados em arquivo (via `sqlite3` nativo)

## Objetivo

Levar o aluno do zero até uma aplicação CRUD funcional. Ao final, o aluno consegue:

- Criar rotas, templates e modelos
- Persistir dados em SQLite
- Continuar aprendendo sozinho

## Como rodar o projeto final

```bash
cd project_starter
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
python run.py
```

Acesse `http://localhost:5000`

## Estrutura do repositório

```
.
├── README.md
├── syllabus.md
├── schedule.md
├── lessons/           # 15 arquivos de aula
├── exercises/         # 15 arquivos de exercício
├── solutions/         # 15 arquivos de solução
├── project_starter/   # código inicial
└── project_solution/  # solução completa
```
