class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    # Методы сравнения
    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec <= other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec >= other.sec


#  Математические операции
c1 = Clock(600)
c2 = Clock(200)
c3 = c1 - c2
print(f"c1 - c2 = {c3.get_format_time()}")
c4 = c1 * c2
print(f"c1 * c2 = {c4.get_format_time()}")
c5 = c1 // c2
print(f"c1 // c2 = {c5.get_format_time()}")
c6 = c1 % c2
print(f"c1 % c2 = {c6.get_format_time()}")
c1 -= c2
print(f"c1 -= c2 = {c1.get_format_time()}")
c1 *= c2
print(f"c1 *= c2 = {c1.get_format_time()}")
c1 //= c2
print(f"c1 //= c2 = {c1.get_format_time()}")
c1 %= c2
print(f"c1 %= c2 = {c1.get_format_time()}")

# Сравнение
print(c3 > c1)
print(c3 >= c1)
print(c3 < c1)
print(c3 <= c1)
