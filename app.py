from flask import Flask, render_template, request, redirect
from database import get_all_tasks, add_task, delete_task, init_db

app = Flask(__name__)

@app.before_first_request
def setup_database():
    init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            add_task(new_task)
        return redirect("/")

    tasks = get_all_tasks()
    title = "Web đầu tiên của mình 🎉"
    return render_template("home.html", title=title, tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect("/")

