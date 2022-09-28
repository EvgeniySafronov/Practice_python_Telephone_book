import sqlite3

def read_sqlite_table(id):                                                       #records вместо id 
    try:
        sqlite_connection = sqlite3.connect('Telep.book.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        #sqlite_select_query = """SELECT * from telephone_book"""
        sql_select_query = """select * from telephone_book where id = ?"""
        cursor.execute(sql_select_query, (id,))                                  #sqlite_select_query
        records = cursor.fetchall()
        print("Вывод по ID:  ", id)                                              #len(records)
        
        for row in records:
            print("Имя:", row[0])
            print("Должность:", row[1])
            print("День рождения:", row[2])
            print("Адрес:", row[3], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
n = input('Введите ID ')
read_sqlite_table(n)