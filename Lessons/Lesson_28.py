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

class Chess(ABC):
    def draw(self):
        print("Нарисовал шахматную доску")

    @abstractmethod
    def move(self):
        ...


