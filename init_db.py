import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Project', 'Content for the first project')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Project', 'Content for the second project')
            )

connection.commit()
connection.close()

