'''
ДЗДДЗДЗДЗДЗДЗДЗ

a = int(input('Введите число от 1 до 99: '))
kop = a
if 11 <= kop <= 14:
	print(a, 'копеек')
elif 1 <= a <= 10 or 15 <= a <= 99:
	kop = kop % 10
	if kop == 1:
		print(a, 'копейка')
	elif 2 <= kop <= 4:
		print(a, 'копейки')
	else:
		print(a, 'копеек')
else:
	print('Значение должно быть от 1 до 99')
'''


# Исключения
'''
try:   
	n = int(input("Введите делимое: "))    
	m = int(input("Введите делитель: "))   
	print(n / m) 
except ValueError:    
	print("Нельзя вводить строки")
except ZeroDivisionError:    
	print("Нельзя делить на 0")
'''

# Циклы
'''
i = 0
while i < 5:
	print("i =", i)
	i += 1
'''
'''
i = 1
while i <= 20:
	if i % 2 == 0:
		print(i)
	i += 1 
'''


# n = input("Введите целое число: ")
# while type(n) is not int:      
# 	try:        
# 		n = int(n) except ValueError:        
# 			print("Число не целое!")        
# 			n = input("Введите целое число: ")if n % 2 == 0:   
# 			print("Четное")
# else:    
# 	print("Нечетное")




# while True:
# 	n = int(input('Введите положительное число: '))
# 	if n < 0:
# 		break

# Задача: найти произведение вводимых пользователем чисел
'''
res = 1
while True:    
	n = int(input("введите  число: "))        
	if n == 0:        
		break    
	res = n * res
print(res)
print("\nЦикл завершен")
'''

i = 1
while i < 10:
	j = 1
	while j < 10:
		print(i, '*', j, '=', i * j, end='\t\t')
		j += 1
	print()
	i += 1		

