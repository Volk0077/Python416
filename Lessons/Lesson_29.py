# __________________________Магические методы ______________
# __repr__
"""
class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):  # отрабатывает когда нет __str__
        return f"{self.__class__}: {self.name}"


cat = Cat("Пушок")
print(cat)
"""


# ________________________Множественное наследование__________________________

'''
class Creature:
    def __init__(self, name):
        self.name = name


class Animal(Creature):
    def sleep(self):
        print(self.name + " is sleeping")


class Pet(Creature):
    def play(self):
        print(self.name + " is playing")


class Dog(Animal, Pet):
    def bark(self):
        print(self.name + " is barking")


dog = Dog("Buddy")
dog.bark()
dog.sleep()
dog.play()
'''



# Задача


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"{self.__x}, {self.__y}"


class Styles:
    def __init__(self, color="red", width=1):
        print("Инициализатор Styles")
        self.color = color
        self.width = width


class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print("Инициализатор Pos")
        self.sp = sp
        self.ep = ep
        # Styles.__init__(self, *args)
        super().__init__(*args)


class Line(Pos, Styles):
    def draw(self):
        print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")


l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
l1.draw()

# _____________Миксины___________
'''

'''
class MixinLog:
    ID = 0

    def __init__(self):
        print("Init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 17:15")


class Goods:
    def __init__(self, name, weight, price):
        print("Init Goods")
        self.name = name
        self.weight = weight
        self.price = price
        super().__init__()

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class Notebook(Goods, MixinLog):
    pass


n = Notebook("HP", 1.5, 35000)
n.print_info()
n.save_sell_log()

