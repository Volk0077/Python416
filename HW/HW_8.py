"""
Вычисление площади фигур
"""

from math import sqrt, pi


print("1-прямоугольник, 2-треугольник, 3-круг")
figure = input("Выберите фигуру: ")

if figure == "1":
    print("Длины сторон прямоугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Площадь: ", round((a * b), 2))
elif figure == "2":
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь:", round(s, 2))
elif figure == "3":
    r = float(input("Радиус круга R = "))
    print("Площадь:", round((pi * r**2), 2))
else:
    print("Ошибка ввода")
