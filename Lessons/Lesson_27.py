# _________________________________Наследование в ООП____________________________

"""
class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width


class Line(Prop):
    def __init__(self, *args):
        print("переопределенный инициализатор Line")
        super().__init__(*args)

    def draw_line(self):
        print(f"Рисовании линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

class Rect(Prop):
    def draw_rect(self):
        print(f"Рисовании прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")

line = Line(Point(1, 2), Point(10, 20))
line.draw_line()

rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()
"""

