# Работа с файлами 2
"""
# f = open('xyz.txt', 'w')
# f.write("This is line1.\nThis is line2.\nThis is line3.") # запись файлов
# f.close

f = open("xyz.txt")
# print(f.read())
print(f.readline())
print(f.readline(8))
print(f.readline())

f.close()
"""
# Замена строчек в файле

"""
file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
#
# f = open(file, "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello world!\n"
# print(read_line)
# f.close()

# f = open(file, "w")
# f.writelines(read_line)
# f.close()



# функция выводит одно длинное слово, либо список из слов

"""
with open("res2.txt", "w") as f:
    f.write(
        "Файл — именованная область данных на носителе информации, используемая как базовый объект взаимодействия с данными в операционных системах."
    )


def longest_words(file):
    with open(file) as text:
        w = text.read().split()
        max_length = len(max(w, key=len))
        res = [word for word in w if len(word) == max_length]
        if len(res) == 1:
            return res[0]
        return res


print(longest_words("res2.txt"))
"""

import os

# print(os.getcwd()) # показывает путь к текущей директории

# print(os.listdir()) # показывает список директорий и файлов


# os.mkdir('folder') # создание папки

# os.rmdir('folder') # удаление папки

# os.makedirs('s1/s2/s3') # создает вложенные папки

# os.remove('xyz.txt') # удаляет файл

# os.rename() # переименовать файл сначала вводится имя файла через запятую переименованное название файла
