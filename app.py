from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

print("THIS IS MY APP.PY")

@app.route('/', methods=['GET', 'POST'])
def home():
    print("Request Method:", request.method)

    if request.method == 'POST':
        subject = request.form['subject']
        task = request.form['task']
        deadline = request.form['deadline']

        connection = sqlite3.connect("study_planner.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO tasks (subject, task, deadline)
        VALUES (?, ?, ?)
        """, (subject, task, deadline))

        connection.commit()
        connection.close()

    connection = sqlite3.connect("study_planner.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks WHERE completed = 0")

    tasks = cursor.fetchall()
    print(tasks)

    connection.close()

    return render_template("index.html", tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)