import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
            ('Gym', 'Glute'))

cur.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
            ('To work', '9am to 6pm'))

connection.commit()
connection.close()