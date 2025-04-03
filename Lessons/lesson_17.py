from random import randint

# def cylinder(r, h):
#     '''Здесь возможно описать функцию'''
#     return 2 * pi * r * (r + h)


# print(cylinder(2, 4))
"""
while True:
    n = input('->')
    if n != '-1':
        print(ord(n))
    else:
        break
"""

# st = 'Test string for me'
# arr = [ord(x) for x in st]
# print('ASCII коды символов:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое:', arr)

# Генерация случайного пароля
"""
SHORTEST = 6
LONGEST = 16
MIN_ASCII = 33
MAX_ASCII = 126

def random_password():
    rand_len = randint(SHORTEST, LONGEST)
    result = ''
    for i in range(rand_len):
        result += chr(randint(MIN_ASCII, MAX_ASCII))
    return result

print('Случайный пароль: ', random_password())
"""

#  Методы строк
# print(dir(str))
"""
s = 'hello, WORLD! I am learning Python'
print(s.capitalize()) # Первый Символ становится заглавным       Hello, world! i am learning python
print(s.lower()) # переводит все символы в нижний регистр
print(s.upper()) # переводит все символы в верхний регистр

print(s.count('h')) # подсчет количества букв
print(s.find('Python')) #Возвращает индекс первого вхождения в элемент
print(s.rfind('Python')) #Возвращает индекс первого вхождения в элемент справа
"""

# поменять элементы местами

"""
st = 'один два'

one = st[:st.find(' ')]
two = st[st.find(' ') + 1:]
res = two + ' ' + one
print(res)

st = "один два"
print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")]) # Короткая запись в одну строку
"""
"""
print('abc123'.isalnum()) # состоит ли строка из букв и цифр
print('abcABC'.isalpha()) # состоит ли строка из букв 
"""


str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
print(str1.replace("N", "P"))  # меняет букву, либо слово
