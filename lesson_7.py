# Метод count - считает количество одинаковых элементов в списке
"""
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
num = a.count(6)
print(num)
"""


# Добавление второй части списка если он длиннее в список С
"""
a = [1, 2, 3]
b = [11, 22, 33, 4, 2]
c = []


for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
for i in range(len(a), len(b)):  # range(3, 5) по индексам
    c.append(b[i])

print(c)
"""
#  Методы списков - удаление
# lst = [11, 1, 22, 2, 33, 3, 55, 66]
"""
lst[5:] = [] # СРЕЗЫ - удаляет элементы из списка с 5го индекса
del lst[2:7] удаляет либо выделенный индекс списка, либо срезом от 2 до 7


lst.remove(22) # удаляет элемент по значению (первое вхождение)

lst.pop() # удаляет последний элемент из списка и может его вернуть если сохранить в переменную
"""
# Задача - удалить элемент из списка
"""
print('Введите элементы списка: ')
a = [int(input("-> ")) for i in range(int(input("n = ")))]
print('Введите индекс: ')
k = int(input('k = '))

a.pop(k)
print(a)
"""
# Генерация случайных данных

import random

"""
print(random.random()) # генерирует число флоат до 1 не включая 1
print(random.randint(1, 10)) # генерирует число в диапазоне целое
print(random.uniform(2.5, 10.5)) # генерирует число в диапазоне вещественное
print(random.randrange(10)) # генерирует как range (star, stop, step)

city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]

# print(random.choice(city_list)) # Меняет одно значений 
# print(random.choice(s))
# print(random.choices(city_list, k=3)) # Меняет несколько значений по параметру к=....
# print(random.choices(s, k=3))

random.shuffle(s) # вперемешку
print(s)


mas = [random.randint(0, 100) for i in range(10)]
print(mas)
"""
