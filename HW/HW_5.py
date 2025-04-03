a = [0] * int(input("Введите количество элементов списка: "))
s = 0
for i in range(len(a)):
    a[i] = int(input("->"))
for i in a:
    if i < 0:
        s += i
print("Сумма отрицательных элементов:", s)
