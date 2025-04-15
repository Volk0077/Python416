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

# ИСправить проверку на число !!!!
'''
class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        super().__init__(color)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, w):
        if isinstance(w, int) and  w > 0:
            self.__width = w
        else:
            raise ValueError('Ширина должна быть положительным числом')
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, h):
        if isinstance(h, int) and h > 0:
            self._height = h
        else:
            raise ValueError('Высота должна быть положительным числом')

    def area(self):
        print(f"Площадь {self.color} прямоугольника:", end=" " )
        return self.__width * self.__height


rect = Rectangle(10, -20, "green")
print(rect.area())
'''


# Задача


class Rect:    
    def __init__(self, width, height):       
        self.width = width        
        self.height = height           

    def show_rect(self):       
        print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")


class RectFon(Rect):
    def __init__(self, width, height, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()
        print("Фон:", self.fon)

# Домашка-----------------------------------------------------------------------------------------------
class RectBorder(Rect):
    ...



shape1 = RectFon(400, 200, "yellow")
shape1.show_rect()
# # Домашка-----------------------------------------------------------------------------------------------
shape2 = RectBorder(600, 300, "1px", 'solid', 'red')