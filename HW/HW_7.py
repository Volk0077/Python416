"""
Заполнить список 10ю случайными элементами, удалить все элементы, расположенные перед минимальным элементом списка
"""

import random

mas1 = [random.randint(0, 100) for i in range(10)]
print(mas1)
mas = mas1.copy()
mas.sort()

minimal = mas[0]
print("Min =", minimal)

ind = mas1.index(minimal)
print("Index min:", ind)
del mas1[:ind]
print(mas1)
