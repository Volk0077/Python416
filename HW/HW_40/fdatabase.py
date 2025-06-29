import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                # Преобразуем кортежи в словари для удобства использования в шаблонах
                menu_items = []
                for item in res:
                    menu_items.append({
                        'id': item[0],
                        'title': item[1],
                        'url': item[2]
                    })
                return menu_items
        except Exception as e:
            print(f"Ошибка чтения из БД: {e}")
        return []
    
    def add_course(self, title, short_description, price):
        self.__cur.execute(
            "INSERT INTO courses (title, short_description, price) VALUES (?, ?, ?)",
            (title, short_description, price)
        )
        self.__db.commit()

    def get_all_courses(self):
        try:
            self.__cur.execute("SELECT id, title, short_description, price FROM courses")
            res = self.__cur.fetchall()
            if res:
                # Преобразуем кортежи в словари для удобства использования в шаблонах
                courses = []
                for item in res:
                    courses.append({
                        'id': item[0],
                        'title': item[1],
                        'short_description': item[2],
                        'price': item[3]
                    })
                return courses
        except Exception as e:
            print(f"Ошибка чтения курсов из БД: {e}")
        return []