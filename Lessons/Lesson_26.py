#  ООП. Метод класса (cls)

# Задача создать класс, представляющий собой банковский счет


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"

#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)

#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

#     @staticmethod
#     def convert(value, rate):
#         return value * rate

#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate

#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate

#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

#     def edit_owner(self, surname):
#         self.surname = surname

#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()

#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val}{Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val}{Account.suffix} было успешно снято")
#         self.print_balance()

#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")

#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")

#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец:{self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent: .0%}")
#         print("-" * 20)


# acc = Account("1234", "Долгих", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()

# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()

# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()

# acc.add_percent()
# print()

# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


import re


class UserData:
    def __init__(self, fio, old, ps, weight):
        self.fio = fio
        self.old = old
        self.password = ps
        self.weight = weight

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()  # ['Волков', 'Игорь', 'Николаевич!!!']
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = "".join(
            re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE)
        )  # ВолковИгорьНиколаевич
        for s in f:
            # print(s.strip(letters))
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or not 14 <= old <= 100:  # old < 14 or old > 100
            raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()  # ['1234', '567890']
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")
            
    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, year):
        self.verify_old(year)
        self.__old = year

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__password = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        self.verify_weight(w)
        self.__weight = w


p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
p1.fio = "Ветров Игорь Николаевич"
print(p1.fio)
print(p1.__dict__)


p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
