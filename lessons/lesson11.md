# Aula 11 - Validação e mensagens

## Pré-requisito

Agora a aplicação já possui uma rota Flask que recebe um formulário. A
validação abaixo acontece no servidor, mesmo que o navegador também valide.

## Objetivos

- validar dados no servidor;
- mostrar uma mensagem para a pessoa usuária;
- manter os valores preenchidos quando houver erro.

Antes de usar `flash()`, configure uma chave secreta na função
`create_app()`:

```python
# app/__init__.py
app.config["SECRET_KEY"] = "dev-secret"
```

Essa configuração não é necessária para iniciar o servidor ou criar rotas. Ela
é necessária porque as mensagens flash usam a sessão do Flask, que precisa de
uma chave para assinar seus dados.

```python
# app/routes.py
from flask import flash, render_template, request, redirect, url_for

name = request.form.get("name", "").strip()
category = request.form.get("category", "").strip()
description = request.form.get("description", "").strip()
if not name or not category:
    flash("Preencha o nome e a categoria.", "error")
    return render_template(
        "items/form.html",
        title="Novo item",
        name=name,
        category=category,
        description=description,
    ), 400

flash("Item criado com sucesso!", "success")
return redirect(url_for("items"))
```

As categorias passadas para `flash()` viram classes CSS no template:

```html
<!-- app/templates/macros.html -->
{% macro flash_messages() %}
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
    <div class="flash-container">
        {% for category, message in messages %}
        <div class="flash flash-{{ category }}">{{ message }}</div>
        {% endfor %}
    </div>
        {% endif %}
    {% endwith %}
{% endmacro %}
```

Adicione ao `style.css`, pois essas classes ainda não existiam nas aulas
anteriores:

```css
/* app/static/css/style.css */
.flash-container { margin-bottom: 1.5rem; }
.flash {
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 0.5rem;
}
.flash-success { background: #d4edda; color: #155724; }
.flash-error { background: #f8d7da; color: #721c24; }
```

Inclua a macro no layout base:

```html
<!-- app/templates/base.html -->
{% from "macros.html" import flash_messages %}
{{ flash_messages() }}
```

O navegador pode validar um formulário, mas a aplicação também precisa validar
os dados recebidos no servidor.

## Template do formulário

Crie o formulário que será reutilizado pelas aulas de criação e edição:

```html
<!-- app/templates/items/form.html -->
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>{{ title }}</h1>

<form method="post" class="form">
    <div class="form-group">
        <label for="name">Nome</label>
        <input type="text" id="name" name="name"
               value="{{ name or '' }}" required>
    </div>

    <div class="form-group">
        <label for="category">Categoria</label>
        <select id="category" name="category" required>
            <option value="">Selecione</option>
            <option value="work" {% if category == "work" %}selected{% endif %}>
                Trabalho
            </option>
            <option value="personal" {% if category == "personal" %}selected{% endif %}>
                Pessoal
            </option>
            <option value="study" {% if category == "study" %}selected{% endif %}>
                Estudo
            </option>
        </select>
    </div>

    <div class="form-group">
        <label for="description">Descrição</label>
        <textarea id="description" name="description">{{ description or '' }}</textarea>
    </div>

    <div class="form-actions">
        <button type="submit" class="btn btn-primary">Salvar</button>
        <a href="{{ url_for('items') }}" class="btn btn-secondary">Cancelar</a>
    </div>
</form>
{% endblock %}
```

Quando a validação falha, a rota renderiza o mesmo template com os valores
recebidos. Assim, a pessoa não precisa preencher o formulário novamente.

## Exercício (10 min)

Adicione validação ao formulário de item:

1. rejeite nome ou categoria vazios;
2. aceite somente as categorias `work`, `personal` e `study`;
3. mostre mensagens em pt-BR com `flash()`;
4. renderize o mesmo formulário com os valores enviados quando houver erro;
5. confirme que a mensagem aparece com o estilo correspondente.

## Checklist

- [ ] `SECRET_KEY` está configurada antes de usar `flash()`
- [ ] A validação acontece no servidor
- [ ] Categorias inválidas são rejeitadas
- [ ] Mensagens de erro e sucesso aparecem
- [ ] Os valores do formulário são preservados após um erro
- [ ] As classes `.flash-*` estão definidas no CSS
