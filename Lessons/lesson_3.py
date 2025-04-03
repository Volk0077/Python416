"""
Условные операторы
"""



# cnt = 5
# if cnt < 10:
# 	cnt += 1

# print(cnt)

# age = int(input("Введите ваш возраст: "))
# if age >= 18:
# 	print("Доступ на сайт разрешен")
# else:
# 	print("Доступ запрещен")

# Задача с треугольниками
"""
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b == c:
	print("Треугольник равносторонний")
elif a == b or b == c or a == c:
	print("Треугольник равнобедренный")
else:
	print("Треугольник разносторонний")
"""
# Вложенные циклы

'''
day = int(input('Введите день недели цифрой: '))
if 1 <= day <= 5:   # day >= 1 and day <= 5:
	print('Рабочий день - ', end = '')
	if day == 1:
		print('Понедельник')
	if day == 2:
		print('Вторник')
	if day == 3:
		print('Среда')
	if day == 4:
		print('Четверг')
	if day == 5:
		print('Пятница')
elif day == 6 or  day == 7:
	print('Выходной день - ', end = '')
	if day == 6:
		print('Суббота')
	if day == 7:
		print('Воскресенье')
else:
	print('В неделе только 7 дней))')

ЗАДАЧА № 2
mes = int(input('Введите номер месяца: '))
if mes == 12 or mes == 1 or mes == 2:
	print('зима')
elif mes == 3 or mes == 4 or mes == 5:
	print('весна')
elif mes == 6 or mes == 7 or mes == 8:
	print('лето')
elif mes == 9 or mes == 10 or mes == 11:
	print('лето')
else:
	print('В году только 12 месяцев))')
'''
# задача на окончания

'''
n = int(input('Введите количество ворон (в диапазоне от 0 до 9): '))
if  0 <= n <= 9:
	print('На ветке ', end = '')
	if n == 1:
		print(n, 'ворона')
	if 2 <= n <= 4:
		print(n, 'вороны')
	if 5 <= n <= 9 or n == 0:
		print(n, 'ворон')
else:
	print('Ошибка ввода')
'''

password = '' # Нужно ввести значение admin, user

# Операторы какие то 
'''
match password:
	case 'admin':
		print('Админ')
	case 'user':
		print('юзер')
	case _:
		print('Пароль неверен')
'''


# Тернарное выражение

# a, b = 1030, 20
# print(a if a < b else b)

