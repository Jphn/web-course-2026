# app/models.py - Database Layer (Production Ready)
import sqlite3
import logging
from flask import g

logger = logging.getLogger(__name__)
DB_PATH = 'app.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
    logger.info('Database initialized')

def list_items(page=1, per_page=10, search=None):
    db = get_db()
    offset = (page - 1) * per_page

    if search:
        sql = '''SELECT * FROM items
                 WHERE name LIKE ? OR description LIKE ?
                 ORDER BY created_at DESC LIMIT ? OFFSET ?'''
        params = (f'%{search}%', f'%{search}%', per_page, offset)
    else:
        sql = 'SELECT * FROM items ORDER BY created_at DESC LIMIT ? OFFSET ?'
        params = (per_page, offset)

    cursor = db.execute(sql, params)
    return cursor.fetchall()

def count_items(search=None):
    db = get_db()
    if search:
        cursor = db.execute(
            'SELECT COUNT(*) as total FROM items WHERE name LIKE ? OR description LIKE ?',
            (f'%{search}%', f'%{search}%')
        )
    else:
        cursor = db.execute('SELECT COUNT(*) as total FROM items')
    return cursor.fetchone()['total']

def get_item(id):
    db = get_db()
    cursor = db.execute('SELECT * FROM items WHERE id = ?', (id,))
    return cursor.fetchone()

def create_item(name, category, description=''):
    db = get_db()
    exists = db.execute('SELECT 1 FROM items WHERE name = ?', (name,)).fetchone()
    if exists:
        logger.warning(f'Duplicate item name attempted: {name}')
        raise ValueError('Item with this name already exists')

    try:
        cursor = db.execute(
            'INSERT INTO items (name, category, description) VALUES (?, ?, ?)',
            (name, category, description)
        )
        db.commit()
        logger.info(f'Item created: id={cursor.lastrowid}, name={name}')
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        logger.warning(f'Integrity error on create: {e}')
        raise ValueError('Item with this name already exists')
    except sqlite3.Error as e:
        logger.error(f'Database error on create: {e}')
        raise

def update_item(id, name, category, description):
    db = get_db()
    exists = db.execute('SELECT 1 FROM items WHERE name = ? AND id != ?', (name, id)).fetchone()
    if exists:
        logger.warning(f'Duplicate item name on update: {name}')
        raise ValueError('Item with this name already exists')

    try:
        db.execute(
            'UPDATE items SET name = ?, category = ?, description = ? WHERE id = ?',
            (name, category, description, id)
        )
        db.commit()
        logger.info(f'Item updated: id={id}')
    except sqlite3.IntegrityError as e:
        logger.warning(f'Integrity error on update: {e}')
        raise ValueError('Item with this name already exists')
    except sqlite3.Error as e:
        logger.error(f'Database error on update: {e}')
        raise

def delete_item(id):
    db = get_db()
    try:
        db.execute('DELETE FROM items WHERE id = ?', (id,))
        db.commit()
        logger.info(f'Item deleted: id={id}')
    except sqlite3.Error as e:
        logger.error(f'Database error on delete: {e}')
        raise