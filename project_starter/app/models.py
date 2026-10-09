# app/models.py - Database Layer
import sqlite3
from flask import g

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

def list_items(search=None):
    db = get_db()
    if search:
        cursor = db.execute(
            'SELECT * FROM items WHERE name LIKE ? OR description LIKE ? ORDER BY created_at DESC',
            (f'%{search}%', f'%{search}%')
        )
    else:
        cursor = db.execute('SELECT * FROM items ORDER BY created_at DESC')
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
        raise ValueError('Item with this name already exists')

    cursor = db.execute(
        'INSERT INTO items (name, category, description) VALUES (?, ?, ?)',
        (name, category, description)
    )
    db.commit()
    return cursor.lastrowid

def update_item(id, name, category, description):
    db = get_db()
    exists = db.execute('SELECT 1 FROM items WHERE name = ? AND id != ?', (name, id)).fetchone()
    if exists:
        raise ValueError('Item with this name already exists')

    db.execute(
        'UPDATE items SET name = ?, category = ?, description = ? WHERE id = ?',
        (name, category, description, id)
    )
    db.commit()

def delete_item(id):
    db = get_db()
    db.execute('DELETE FROM items WHERE id = ?', (id,))
    db.commit()