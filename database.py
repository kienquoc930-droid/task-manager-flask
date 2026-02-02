import sqlite3

DB_PATH = "/tmp/tasks.db"   # ⚠️ BẮT BUỘC /tmp

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

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

def add_task(title):
    conn = get_connection()
    conn.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()
