# Продолжение ООП____________________________________________


# Задача
import math

"""
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    def set_width(self, width):
        if Rectangle.__check_value(width):
            self.__width = width

    def set_length(self, length):
        if Rectangle.__check_value(length):
            self.__length = length

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_area(self):
        return self.__length * self.__width

    def get_perimetr(self):
        return 2 * (self.__length + self.__width)

    def get_hypotenuse(self):
        return round(math.sqrt(self.__length**2 + self.__width**2), 2)

    def get_draw(self):
        for i in range(self.__length):
            for j in range(self.__width):
                print("*", end="")
            print()


r1 = Rectangle(4, 12)
r1.set_width(9)
r1.set_length(3)
print("Длина прямоугольника:", r1.get_length())
print("Ширина прямоугольника:", r1.get_width())
print("Площадь прямоугольника:", r1.get_area())
print("Периметр прямоугольника:", r1.get_perimetr())
print("Гипотенуза прямоугольника:", r1.get_hypotenuse())
r1.get_draw()
"""

class Point:
    __slots__ = ["x", "y"] # не разрешает добавить значения кроме указанных

    def __init__(self, x , y):
        self.x = x
        self.y = y


p1 = Point(5, 10)
p1.z = 1
# print(p1.__dict__)