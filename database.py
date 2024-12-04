import sqlite3

def create_db():
    conn = sqlite3.connect('notes_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            login TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()
create_db()


def connect_db():
    conn = sqlite3.connect('notes_app.db')
    return conn