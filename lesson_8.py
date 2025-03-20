import random
import math
from math import pi
import time

# перемещение мах значения в начало списка
"""
mas = [random.randint(0, 100) for i in range(10)]
print(mas)
maximum = max(mas)
print('Max =', maximum)
mas.remove(maximum)
mas.insert(0, maximum)
print(mas)
"""
# двумерная таблица 2 варианта
"""
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(m)

print("Вариант 1")
for row in range(len(m)):
    for col in range(len(m[row])):
        print(m[row][col], end="\t")
    print()


print("Вариант 2")
for row in m:
    for x in row:
        print(x, end="\t")
    print()
"""
# Модули. Модуль math
# Чтобы записать короткое имя модуля import math as m
# from math import sqrt, ceil, floor - импортируем 3 метода чтобы не нагружать программу
"""
print(math.sqrt(4)) # корень из числа
print(math.ceil(3.2))  # округление в большую сторону
print(math.floor(3.8)) # округление в меньшую сторону
"""

# Задача найти радиус
"""
radius = int(input('Введите радиус окружности: '))

print('Длинна окружности:', 2 * pi *radius)
"""

#  Модуль TIME
"""
print(time.time())
print(time.ctime())
"""


start = time.monotonic()
pause = 5
print("Программа запущена")
time.sleep(pause)
result = time.monotonic() - start
print("Программа выполнен за", result, "секунд")
