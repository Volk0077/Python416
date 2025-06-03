# Базы данных
# Создание файла базы данных 2 способа
import sqlite3

# Первый способ
# con = sqlite3.connect("profile.db")
# cur = con.cursor() 

# cur.execute("")

# con.close()

# Второй способ
with sqlite3.connect("users.db") as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    #             id  INTEGER PRIMARY KEY AUTOINCREMENT,
    #             name TEXT NOT NULL,
    #             phone BLOB NOT NULL DEFAULT "+7 909 123 45 56",
    #             age INTEGER CHECK(age > 0 AND age < 100),
    #             email TEXT UNIQUE NOT NULL
    #             )""")

    #  Манипуляции с таблицей


    #  Переименование таблицы
    # cur.execute("""
    #             ALTER TABLE users
    #             RENAME TO person_table; 

    #             """)
    
    # Добавление нового столбца
    # cur.execute("""
    #             ALTER TABLE person_table
    #             ADD COLUMN address TEXT; 
    #             """)

    # Переименовать столбец
    # cur.execute("""
    #             ALTER TABLE person_table
    #             RENAME COLUMN address TO home_addrees;
    #             """)
    
    # Удалить столбец
    # cur.execute("""
    #             ALTER TABLE person_table
    #             DROP COLUMN home_addrees;
    #             """)