import os

search_file = input("Введите имя файла с расширением: ")
file = r"C:\Users\honor\Desktop\Python416\s1\s2\s3"

found = False  # Флаг для отслеживания, найден ли файл
for root, dirs, files in os.walk(file):
    if search_file in files:
        found = True
        file_path = os.path.join(root, search_file)
        print(
            f"Файл найден: {file_path}",
            "-",
            "Последний доступ:",
            os.path.getatime(file_path),
            "сек",
        )
        break  # Прекращаем поиск после нахождения файла

if not found:
    print("Нет такого файла")
