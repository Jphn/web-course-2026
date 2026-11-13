from flask import flash, redirect, render_template, request, url_for

from .models import create_item, delete_item, get_item, list_items, update_item


def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/items/")
    def items():
        return render_template("items/list.html", items=list_items())

    @app.route("/items/new", methods=["GET", "POST"])
    def new_item():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            category = request.form.get("category", "").strip()
            description = request.form.get("description", "").strip()

            if not name or not category:
                flash("Preencha o nome e a categoria.", "error")
            elif category not in ("work", "personal", "study"):
                flash("Escolha uma categoria válida.", "error")
            else:
                try:
                    create_item(name, category, description)
                    flash("Item criado com sucesso!", "success")
                    return redirect(url_for("items"))
                except ValueError as error:
                    flash(str(error), "error")

            return render_template(
                "items/form.html",
                title="Novo item",
                name=name,
                category=category,
                description=description,
            ), 400

        return render_template("items/form.html", title="Novo item")

    @app.route("/items/<int:id>/edit", methods=["GET", "POST"])
    def edit_item(id):
        item = get_item(id)
        if item is None:
            return "Item não encontrado", 404

        if request.method == "POST":
            name = request.form.get("name", "").strip()
            category = request.form.get("category", "").strip()
            description = request.form.get("description", "").strip()

            if not name or not category:
                flash("Preencha o nome e a categoria.", "error")
            elif category not in ("work", "personal", "study"):
                flash("Escolha uma categoria válida.", "error")
            else:
                try:
                    update_item(id, name, category, description)
                    flash("Item atualizado com sucesso!", "success")
                    return redirect(url_for("items"))
                except ValueError as error:
                    flash(str(error), "error")

            return render_template(
                "items/form.html",
                title="Editar item",
                item=item,
                name=name,
                category=category,
                description=description,
            ), 400

        return render_template(
            "items/form.html",
            title="Editar item",
            item=item,
            name=item["name"],
            category=item["category"],
            description=item["description"],
        )

    @app.post("/items/<int:id>/delete")
    def delete_item_route(id):
        if get_item(id) is None:
            return "Item não encontrado", 404
        delete_item(id)
        flash("Item excluído com sucesso!", "success")
        return redirect(url_for("items"))
