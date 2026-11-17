# Aula 13 - Criar e listar itens

## Pré-requisito

Na Aula 12, a aplicação passou a criar a tabela `items`. Agora vamos inserir
registros e mostrar os dados salvos. O template
`app/templates/items/form.html` foi criado na Aula 11 e será reutilizado para
o cadastro.

## Objetivos

- buscar registros no banco;
- inserir um registro;
- mostrar uma lista no template;
- redirecionar depois de um POST.

## Funções do modelo

Em `app/models.py`, adicione a função para listar os itens:

```python
# app/models.py
def list_items():
    return get_db().execute(
        "SELECT * FROM items ORDER BY created_at DESC, id DESC"
    ).fetchall()
```

Para criar um item, use parâmetros separados e confirme a alteração com
`commit()`:

```python
# app/models.py
def create_item(name, category, description):
    db = get_db()
    db.execute(
        "INSERT INTO items (name, category, description) VALUES (?, ?, ?)",
        (name, category, description),
    )
    db.commit()
```

Os pontos de interrogação são preenchidos pelos valores da tupla. Não monte
SQL concatenando texto recebido do formulário.

## Rotas

Em `app/routes.py`, passe a lista para o template:

```python
# app/routes.py
def register_routes(app):
    @app.route("/items/")
    def items():
        return render_template("items/list.html", items=list_items())
```

A rota do formulário recebe os dados no POST, cria o item e volta para a lista:

```python
# app/routes.py
def register_routes(app):
    @app.route("/items/new", methods=["GET", "POST"])
    def new_item():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            category = request.form.get("category", "").strip()
            description = request.form.get("description", "").strip()
            create_item(name, category, description)
            flash("Item criado com sucesso!", "success")
            return redirect(url_for("items"))

        return render_template("items/form.html", title="Novo item")
```

Nesta primeira versão, use os campos já criados nas aulas anteriores. A
validação e as mensagens flash da Aula 11 continuam sendo responsabilidade da
rota; execute essa validação antes de chamar `create_item()`.

## Template da lista

Em `app/templates/items/list.html`, percorra os registros recebidos:

```html
<!-- app/templates/items/list.html -->
{% extends "base.html" %}

{% block title %}Itens{% endblock %}

{% block content %}
<h1>Itens</h1>
<a href="{{ url_for('new_item') }}" class="btn btn-primary">Novo item</a>

<div class="card">
    {% for item in items %}
    <article>
        <h2>{{ item.name }}</h2>
        <p>{{ item.description or "-" }}</p>
        <span class="badge badge-{{ item.category }}">
            {% if item.category == "work" %}Trabalho
            {% elif item.category == "personal" %}Pessoal
            {% else %}Estudo{% endif %}
        </span>
    </article>
    {% else %}
    <p>Nenhum item cadastrado.</p>
    {% endfor %}
</div>
{% endblock %}
```

## Exercício (10 min)

Conecte a página `/items/` ao banco, implemente a criação de um item e
confirme que o novo registro aparece na lista depois do envio do formulário.

## Checklist

- [ ] `list_items()` executa um `SELECT`
- [ ] `create_item()` usa parâmetros e chama `commit()`
- [ ] `/items/` passa os itens para o template
- [ ] `/items/new` aceita GET e POST
- [ ] o POST redireciona para a lista
- [ ] a lista mostra os itens salvos
