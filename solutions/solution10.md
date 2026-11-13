# Solução 10 - Formulário

```python
@app.route("/hello", methods=["GET", "POST"])
def hello():
    name = request.form.get("name", "").strip()
    return render_template("hello.html", name=name)
```
