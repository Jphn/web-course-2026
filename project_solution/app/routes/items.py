# app/routes/items.py - Items CRUD Routes (with Pagination)
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import list_items, get_item, create_item, update_item, delete_item, count_items

items_bp = Blueprint('items', __name__, url_prefix='/items')

@items_bp.route('/')
def list():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('q', '').strip()
    per_page = 10

    items = list_items(page=page, per_page=per_page, search=search if search else None)
    total = count_items(search=search if search else None)
    total_pages = (total + per_page - 1) // per_page

    return render_template('items/list.html',
        items=items,
        page=page,
        total_pages=total_pages,
        total=total,
        search=search)

@items_bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()

        errors = []
        if not name:
            errors.append('Name is required')
        elif len(name) > 100:
            errors.append('Name too long (max 100 chars)')
        if not category:
            errors.append('Category is required')
        elif category not in ['work', 'personal', 'study']:
            errors.append('Invalid category')
        if description and len(description) > 500:
            errors.append('Description too long (max 500 chars)')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('items/form.html', title='New Item',
                name=name, category=category, description=description), 400

        try:
            create_item(name, category, description)
            flash(f'Item "{name}" created!', 'success')
            return redirect(url_for('items.list'))
        except ValueError as e:
            flash(str(e), 'error')
            return render_template('items/form.html', title='New Item',
                name=name, category=category, description=description), 400

    return render_template('items/form.html', title='New Item')

@items_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    item = get_item(id)
    if not item:
        flash('Item not found', 'error')
        return redirect(url_for('items.list'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()

        errors = []
        if not name:
            errors.append('Name is required')
        elif len(name) > 100:
            errors.append('Name too long (max 100 chars)')
        if not category:
            errors.append('Category is required')
        elif category not in ['work', 'personal', 'study']:
            errors.append('Invalid category')
        if description and len(description) > 500:
            errors.append('Description too long (max 500 chars)')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('items/form.html', title='Edit Item', item=item,
                name=name, category=category, description=description), 400

        try:
            update_item(id, name, category, description)
            flash(f'Item "{name}" updated!', 'success')
            return redirect(url_for('items.list'))
        except ValueError as e:
            flash(str(e), 'error')
            return render_template('items/form.html', title='Edit Item', item=item,
                name=name, category=category, description=description), 400

    return render_template('items/form.html', title='Edit Item', item=item,
        name=item.name, category=item.category, description=item.description)

@items_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    item = get_item(id)
    if not item:
        flash('Item not found', 'error')
        return redirect(url_for('items.list'))

    name = item.name
    delete_item(id)
    flash(f'Item "{name}" deleted!', 'success')
    return redirect(url_for('items.list'))