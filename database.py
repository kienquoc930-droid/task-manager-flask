import sqlite3

DB_NAME = "tasks.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return tasks

def add_task(name):
    conn = get_db()
    conn.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
def get_task(task_id):
    conn = get_db()
    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    conn.close()
    return task


def update_task(task_id, name):
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET name = ? WHERE id = ?",
        (name, task_id)
    )
    conn.commit()
    conn.close()
