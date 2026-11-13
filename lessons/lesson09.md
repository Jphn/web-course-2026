# Aula 9 - Rotas e navegação

## Objetivos

- criar mais de uma rota;
- renderizar templates;
- gerar links com `url_for`.

```python
from flask import render_template

@app.route("/about")
def about():
    return render_template("about.html")
```

No template, prefira:

```html
<a href="{{ url_for('about') }}">Sobre</a>
```

Assim o caminho fica definido em um só lugar. Nesta aula, a turma conecta as
páginas inicial, sobre, contato e itens.
