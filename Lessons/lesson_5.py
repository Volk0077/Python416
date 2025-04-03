# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         continue
# else:
#     print('Конец цикла')

# Вложенные циклы

'''
for i in range(3):
    print('+++')
    for j in range(2):
        print('------')
'''
# Прямоугольник из звездочек

'''
w = 4
h = 17

for i in range(h):
    for j in range(w):
        if i == 0 or i == h - 1 or j == 0 or j == w - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
# Список (list) обозначается как []
'''
string = [letter * 2 for letter in 'Python']
print(string)

for letter in 'Python':
    print(letter * 2, end='\t')
'''

# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]


# Длина списка
'''
print(len(nums))
'''

# Сложение умножение списков
'''
n = nums + nums2
print(n)
'''

# списки в одну строку
# [выражение for переменная in какая то последовательность]
'''
n = 5
a = [i ** 2 for i in range(1, n + 1)]
print(a)
'''

# Спсики в одну строку, короткая запись ниже 

a = [0] * int(input('Введите количество элементов списка: '))
print(a)
for i in range(len(a)):
    a[i] = int(input('->'))
print(a)
'''
a = [int(input('->')) for i in range(int(input('Введите количество элементов списка: ')))]
print(a)
'''

