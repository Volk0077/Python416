import sqlite3

with sqlite3.connect("db_3.db") as con:
    cur = con.cursor()
    cur.execute('''
SELECT * FROM T1
LIMIT 2, 5
''')
    # Вывод содержимого в принт
    # for res in cur:
    #     print(res)

# # Вывод всего содержимого в принт как список кортежей в одну строку
    # res = cur.fetchall()
    # print(res)
# ВЫвод первой строки содержимого как кортеж
    res1 = cur.fetchone()
    print(res1)

    res2 = cur.fetchmany()
    print(res2)