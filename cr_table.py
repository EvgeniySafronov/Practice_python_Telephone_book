import sqlite3

try:
    sqlite_connection = sqlite3.connect('Telep.book.db')
    sqlite_create_table_query = '''CREATE TABLE telephone_book (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                post text NOT NULL,
                                birth_date datetime,
                                adress REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")