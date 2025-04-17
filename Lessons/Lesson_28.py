# _____________________Абстрактные методы________________________

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Prop:
    def __init__(self, sp, ep, color, width):
        self.sp = sp
        self.ep = ep
        self.color = color
        self.width = width

    def draw(self):
        raise NotImplementedError("В дочернем классе должен быть метод draw()") # Абстрактный метод


class Line(Prop):
    def draw(self):
        print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")


class Rect(Prop):
    def draw(self):
        print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.width}")


class Ellipse(Prop):
    def draw(self):
        print(f"Рисование эллипса: {self.sp}, {self.ep}, {self.color}, {self.width}")


shapes = list()
shapes.append(Line(Point(0, 0), Point(10, 10), "yellow", 10))
shapes.append(Line(Point(10, 10), Point(20, 20), "red", 6))
shapes.append(Rect(Point(50, 50), Point(70, 70), "blue", 4))
shapes.append(Ellipse(Point(80, 80), Point(100, 100), "green", 3))

for i in shapes:
    i.draw()
'''


from abc import ABC, abstractmethod
from math import pi

# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")

#     @abstractmethod
#     def move(self):
#         ...

# Задача класс стол и дочерние классы прямоугольный сто и круглый стол 


class Table:
    def __init__(self, width=None, length=None, radius=None):  # 20, None, None
        if radius is None:
            if length is None:
                self.width = self.length = width
            else:
                self.width = width
                self.length = length        
        else:
            self.radius = radius

    def calc_area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод calc_area ()")
    
class RectangleTable(Table):
    def calc_area(self):
        return self.width * self.length
    
class RoundTable(Table):
    def calc_area(self):
        return round(pi * self.radius ** 2, 2)
    

t = RectangleTable(20, 10)
print(t.__dict__)
print(t.calc_area())

t1 = RectangleTable(20)
print(t1.__dict__)
print(t1.calc_area())

t2 = RoundTable(radius=20)
print(t2.__dict__)
print(t2.calc_area())
