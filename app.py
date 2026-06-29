from flask import Flask, render_template, request, redirect

from database.db_helper import (
    add_task,
    get_pending_tasks,
    complete_task,
    get_completed_tasks,
    delete_task,
    search_tasks,
    get_task,
    update_task
)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        subject = request.form['subject']
        task = request.form['task']
        deadline = request.form['deadline']

        add_task(subject, task, deadline)

    search = request.args.get("search")

    if search:
        tasks = search_tasks(search)
    else:
        tasks = get_pending_tasks()
    completed_tasks = get_completed_tasks()

    return render_template(
        "index.html",
        tasks=tasks,
        completed_tasks=completed_tasks,
        total_tasks=len(tasks) + len(completed_tasks),
        pending_count=len(tasks),
        completed_count=len(completed_tasks)
    )


@app.route('/complete/<int:task_id>')
def complete(task_id):

    complete_task(task_id)

    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):

    delete_task(task_id)

    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):

    if request.method == 'POST':
        subject = request.form['subject']
        task = request.form['task']
        deadline = request.form['deadline']

        update_task(task_id, subject, task, deadline)

        return redirect('/')

    task = get_task(task_id)

    return render_template("edit.html", task=task)

if __name__ == '__main__':
    app.run(debug=True)

