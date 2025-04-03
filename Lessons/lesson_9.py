# Кортежи


# a = 1, 2, 3, 4, 5

from random import randint


# print(tuple(i for i in range(10)))


# Пользователь вводит значения
"""
print(tuple(input('->') for i in range(5)))
"""


# Рандомные значения
"""
print(tuple(randint(50, 100) for i in range(5)))
"""


# Задача 2.jpg
'''
def slicer(tpl, el): 
    if el in tpl:
        if tpl.count(el) == 1:
            return tpl[tpl.index(el):]
        else:
            first = tpl[tpl.index(el):]
            second = tpl.index(el, first + 1) + 1
            return tpl[first:second]
    else:
        return ()


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
'''
#  Распаковка кортежа
'''
def get_user():
    name = 'Tom'
    age = 22
    is_married = False
    return name, age, is_married

# user = get_user()
# print(user)     first_name, year, married = user, ЛИБО......
first_name, year, married = get_user()
print(first_name)
print(year)
print(married)
'''
#  Вложенные кортежи  и их распаковка
'''
countries = (    ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),    ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
    )

print(countries)
for country in countries:    
    country_name, country_population, cities = country    
    print("\nСтрана: ", country_name, ", население = ",  country_population, sep="")    
    for city in cities:        
        city_name, city_population = city        
        print("\tГород: ", city_name, ", население = ", city_population, sep="")
'''

# Задача посчитать количество элементов
'''
tpl = tuple(input('Введите строку: '))
print(tpl)

lst = []
for i in range(len(tpl)):
    if tpl[i] not in lst:
        lst.append(tpl[i])

print(lst)
for i in range(len(lst)):
    print('Количество', lst[i], '=', tpl.count(lst[i]))
'''


def check_password(password):
    if len(password) >= 8:
        return True
    return False


p = input