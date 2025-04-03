# a = list(range(10, 100, 10))
# print(a)

# for i in range(len(a)):
#     print(a[i] + 2, end=' ')

#  Найти все четные индексы

# a = [int(input('->')) for i in range(int(input('n = ')))]
"""
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')
"""

# ИЛИ же....
"""
for i in range(0, len(a), 2):
    print(a[i], end=' ')
"""
# Вывод четных элементов и сложение нечетных элементов списка
"""
n = list(range(21, 41))
print(n)
k = s = 0
for i in range(len(n)):
    if n[i] % 2 == 0:
        k += 1
    else:
        s += n[i]

print("Количество четных элементов:", k)
print("Сумма нечетных элементов:", s)

"""
# Срезы в списках
# список[start:stop:step]
"""
s = [9, 7, 2, 1, 17]
print(s[1:4])

lst = list(range(1, 8))
print(lst)
print(lst[::-1])
print(lst[::2])
print(lst[1::2])
print(lst[:1])
print(lst[::-7])
print(lst[-1:])
print(lst[3:4])
print(lst[4:7])
print(lst[4:])
print(lst[4:1:-1])
print(lst[2:5])
"""

# Методы списков
# print(dir(list)) # dir показывает методы
"""
lst = list(range(1, 8))
print(lst)
lst.append(99)  # добавляет элемент в конец списка
print(lst)
lst.extend([1, 2, 3]) # добавляет несколько элементов в конец списка
print(lst)
lst.insert(0, 100) # (0 - индекс, 100 - значение) Добавляет значение в определенный индекс, остальные элементы смещаются
print(lst)
"""
# добавление в список циклом
"""
s = []
n = int(input('Количество элементов списка: '))
for num in range(n):
    x = int(input('Введите число: '))
    # s. append(x)  в конец списка или.....

    s. insert(0, x) # в начало списка
print(s)
"""
# Отобрать похожие элементы из двух списков
# вариант 1

a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]  # 5, 9, 2, 1, 4, 3, 4, 2
# b = [4, 2, 1, 3, 7, 2]
# c = []
"""
for i in a:
    for j in b:
        if i in c:
            continue # для исключения еще одного дубликата из списка а
        if i == j:
            c.append(i)
            break # для того чтобы не выводить 2 еще раз - прекратить вложенный цикл при совпадении
print(c)
"""
#  вариант 2

for el in a:
    if el not in c and el in b:
        c.append(el)
print(c)
