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


def db_table_notes():
    conn = sqlite3.connect('notes_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id_note INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title_note TEXT NOT NULL,
            text_note TEXT NOT NULL,
            date_created  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) 
        )
    ''')
    conn.commit()
    conn.close()


db_table_notes()


def connect_db():
    conn = sqlite3.connect('notes_app.db')
    return conn
