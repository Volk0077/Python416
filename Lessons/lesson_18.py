# Вывести инициалы из ФИО
'''
s = input('Введите ФИО: ').split()
print(s)
print(f'{s[0]} {s[1][0]}. {s[2][0]}.')
'''


# Регулярные выражения----------------------------------------------------------------------------


import re 

s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.'

reg = 'я'
print(re.findall(reg, s)) # возвращает список совпадений с шаблоном

print(re.search(reg, s)) # возвращает Первое совпадение


