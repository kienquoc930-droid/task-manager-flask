import sqlite3

def get_connection():
    conn = sqlite3.connect("tasks.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def get_all_tasks():
    conn = get_connection()
    return conn.execute("SELECT * FROM tasks").fetchall()


def add_task(name):
    conn = get_connection()
    conn.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
    conn.commit()
