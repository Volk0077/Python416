"""
Вводится количество студентов и балл для каждого. Программа определяет средний балл и выводит студентов с баллом выше среднего
"""

student = {}

n = int(input("Количество студентов: "))
summa = 0
for i in range(n):
    name = input(str(i + 1) + "-й студент: ")
    point = int(input("Балл: "))
    student[name] = point
    summa += point

average = summa / n

print("Средний балл: ", round(average), ". Студенты с баллом выше среднего: ", sep="")

for i in student:
    if student[i] > average:
        print(i)
