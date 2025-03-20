# Словари

# Задача получить два первых элемента словаря
"""
d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
print(
    {k: v for k, v in d.items() if v <= 2}
)  # решение - постановка условия меньше 2 в конце
"""
"""
lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]

d = dict()
s = None

for i in lst:
    if type(i) is str:
        d[i] = []
        s = i
    else:
        d[s].append(i)

print(d)

"""

# Функция zip объединяет несколько объектов
'''
d = dict(zip([1, 2, 3], ["one", "two", "three"])) 
print(d)
d = dict(zip([1, 2, 3], ["one", "two", "three"]))


lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
'''


letter = ['b', 'a', 'd', 'c']
number = [3, 4, 1, 2]
d = dict(zip(letter, number))
print(d)

d1 = list(zip(letter, number))
print(d1)
d1.sort()
print(d1)