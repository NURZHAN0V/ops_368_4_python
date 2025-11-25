import sqlite3

conn = sqlite3.connect('.tmp/clients.db')
cursor = conn.cursor()

# создать таблицу users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        telegram TEXT NOT NULL
    )
''')

def client_add_db(name, phone, telegram):
    # добавить пользователя
    conn = sqlite3.connect('.tmp/clients.db')
    cursor = conn.cursor()

    print(name, phone, telegram)
    cursor.execute('INSERT INTO clients (name, phone, telegram) VALUES (?, ?, ?)', (name, phone, telegram))
    conn.commit()

    # закрываем базу данных
    conn.close()

def client_read_db():
    # получить всех пользователей
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

conn.close()