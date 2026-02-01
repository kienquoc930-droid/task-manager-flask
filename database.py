import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = get_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return tasks
