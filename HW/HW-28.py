from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side * self.side

    def draw(self):
        return ("* " * self.side + "\n") * self.side

    def info(self):
        print(
            f"=== Квадрат ===\nСторона: {self.side}\nЦвет:{self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n"
        )


class Rectangle(Shape):
    def __init__(self, color, width, length):
        super().__init__(color)
        self.width = width
        self.length = length

    def get_perimeter(self):
        return (self.width + self.length) * 2

    def get_area(self):
        return self.width * self.length

    def draw(self):
        return ("* " * self.length + "\n") * self.width

    def info(self):
        print(
            f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет:{self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n"
        )


class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        p = self.get_perimeter() / 2
        return round(
            math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2
        )

    def draw(self):
        rows = []
        for i in range(self.side2):
            rows.append(" " * i + "*" * (self.side1 - 2 * i))
        return "\n".join(reversed(rows))

    def info(self):
        print(
            f"=== Треугольник ===\nСторона1: {self.side1}\nСторона2: {self.side2}\nСторона3: {self.side3}\nЦвет:{self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n"
        )


sq = Square("red", 3)
sq.info()
rect = Rectangle("green", 3, 7)
rect.info()
tr = Triangle("yellow", 11, 6, 6)
tr.info()
