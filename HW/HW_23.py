class Squares:
    __count = 0

    @staticmethod
    def get_count():
        return Squares.__count

    @staticmethod
    def area_triangle_geron(a, b, c):
        Squares.__count += 1
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    @staticmethod
    def area_triangle(a, h):
        Squares.__count += 1
        return 0.5 * a * h
        Squares.__count += 1

    @staticmethod
    def area_square(a):
        Squares.__count += 1
        return a**2

    @staticmethod
    def area_rectangle(a, b):
        Squares.__count += 1
        return a * b


print("Площадь треугольника по формуле Герона:", Squares.area_triangle_geron(3, 4, 5))
print("Площадь треугольника через основание и высоту:", Squares.area_triangle(6, 7))
print("Площадь квадрата:", Squares.area_square(7))
print("Площадь прямоугольника:", Squares.area_rectangle(2, 6))

print("Количество подсчетов площади:", Squares.get_count())
