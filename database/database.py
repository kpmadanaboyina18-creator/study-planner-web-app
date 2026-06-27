import sqlite3

connection = sqlite3.connect("study_planner.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    task TEXT NOT NULL,
    deadline TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")

connection.commit()
connection.close()

print("Database Created Successfully!")