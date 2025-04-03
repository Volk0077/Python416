# Словари

# Задача добавть продукты и исключить какую - то позицию
"""
d = {i: input('->') for i in range(1, 5)}
print(d)
dislike = int(input('Какой элемент исключить: '))
del d[dislike]
print(d)
"""


#  Задача - изменить количество товара в шт.
"""
goods = {      # Создаем словарь как список товаров, количество, и цену за них
    "1": ["Core-i3-4330", 9, 4500],
    "2": ["Core i5-4670K", 3, 8500],
    "3": ["AMD FX-6300", 6, 3700],
    "4": ["Pentium G3220", 8, 2100],
    "5": ["Core i5-3450", 5, 6400],
}

for i in goods: # выводим первоначальное количество товара
    print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб.', sep='')

while True: # заменяем количество шт. 
    n = input('№: ')
    if n  == '0': # Выход из цикла
        break
    else:
        if n in goods:
                while True:
                    try:
                        count = int(input('Количество: '))
                        goods[n][1] += count # += count складывает новое значение с остатком
                    except ValueError:
                        print('Значение некорректно. Введите число')
        else:
            print('Такого ключа не существует: ')

for i in goods:
    print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб.', sep='')
"""


# Методы словарей

d = {"A": 1, "B": 2, "C": 3}
'''
print(d.keys())  # Список ключей
print(d.values())  # Список значений
print(d.items())  # список ключей  и значений

for i, j in d.items():
    print(i, ":", j)
'''


# Задача 
'''
d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
new_d = dict()
new_d['name'] = d.pop('name')
new_d['salary'] = d.pop('salary')
print(d)
print(new_d)
'''

'''
d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}

d['Location'] = d.pop('city')

print(d)
'''


d = {    "first": {        1: "one",        2: "two",        3: "three"    },    "second": {        4: "four",        5: "five"    }}print(d)