from flask import Flask, render_template
from database import get_all_tasks, init_db

app = Flask(__name__)

# 🚨 DÒNG QUAN TRỌNG
init_db()

from database import get_task, update_task
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_task = request.form['task']
        if new_task:
            add_task(new_task)
        return redirect('/')

    tasks = get_all_tasks()
    title = "Web đầu tiên của mình 🎉"
    return render_template('home.html', title=title, tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect('/')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        new_name = request.form['task']
        if new_name:
            update_task(task_id, new_name)
        return redirect('/')

    task = get_task(task_id)
    return render_template('edit.html', task=task)




if __name__ == '__main__':
    app.run()
