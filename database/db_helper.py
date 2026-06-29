import sqlite3

DATABASE = "study_planner.db"


def add_task(subject, task, deadline):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks (subject, task, deadline)
        VALUES (?, ?, ?)
    """, (subject, task, deadline))

    connection.commit()
    connection.close()


def get_pending_tasks():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM tasks
        WHERE completed = 0
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def complete_task(task_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()

def get_completed_tasks():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM tasks
        WHERE completed = 1
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def delete_task(task_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()
def search_tasks(keyword):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE completed = 0
        AND (
            subject LIKE ?
            OR task LIKE ?
        )
    """, (f"%{keyword}%", f"%{keyword}%"))

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def get_task(task_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM tasks
        WHERE id = ?
    """, (task_id,))

    task = cursor.fetchone()

    connection.close()

    return task


def update_task(task_id, subject, task, deadline):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET subject = ?, task = ?, deadline = ?
        WHERE id = ?
    """, (subject, task, deadline, task_id))

    connection.commit()
    connection.close()