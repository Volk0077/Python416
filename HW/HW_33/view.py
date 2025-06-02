class UserInterface:
    def wait_user_answer(self):
        print(" Редактирование данных каталога фильмов ".center(50, "="))
        print("Действия с фильмами:")
        print(
            "1 - добавление фильма"
            "\n2 - каталог фильмов"
            "\n3 - просмотр определенного фильма"
            "\n4 - удаление фильма"
            "\nq - выход из программы"
        )
        user_answer = input("Выберите вариант действия: ")
        print("=" * 50)
        return user_answer

    def add_user_movie(self):
        dict_movie = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None,
        }
        print(" Добавление фильма: ".center(50, "="))
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key} фильма:")
        print("=" * 50)
        return dict_movie

    def show_all_movies(self, movies):
        print(" Каталог фильмов: ".center(50, "|"))
        for ind, movie in enumerate(movies, 1):
            print(f"{ind}. {movie}")
        print("|" * 50)

    def get_user_movie(self):
        print(" Ввод названия фильма: ".center(50, "|"))
        user_movie = input("Введите название фильма: ")
        print("|" * 50)
        return user_movie
    
    def show_single_movie(self, movie):
        print(" Информация о фильме: ".center(50, "|"))
        for key in movie:
            print(f"{key} фильма - {movie[key]}")
        print("|" * 50)

    def show_incorrect_title_error(self, user_movie):
        print(f"Фильма с названием {user_movie} в базе нет.".center(50, "-"))
        print("|" * 50)

    def remove_single_movie(self, movie_title):
        print(f"Фильм {movie_title} успешно удален.".center(50, "-"))
        print("|" * 50)

    def show_not_available_answer_error(self, answer):
        print(" Сообщение об ошибке: ".center(50, "|"))
        print("Вы ввели недопустимый вариант. Повторите ввод.".center(50, "="))
        print("|" * 50)