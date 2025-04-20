# для использования декоратора @property, нужно раскомментировать строки36-45, 105 и закомментировать строки 47-51,101


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    # Изменение процента с использованием @property
    # @property
    # def percent(self):
    #     return self._percent

    # @percent.setter
    # def percent(self, value):
    #     if 0 <= value <= 1:
    #         self._percent = value
    #     else:
    #         raise ValueError("Процент должен быть в диапазоне от 0 до 1.")
    # Изменение процента с использованием сет и гет методов
    def set_percent(self, percent):
        if 0 <= percent <= 1:
            self.percent = percent
        else:
            print("Ошибка: процент должен быть в диапазоне от 0 до 1.")

    def get_percent(self):
        return self.percent

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


# Изменение процента с использованием сет и гет методов
acc = Account("12345", "Долгих", 0.03, 1000)
acc.print_balance()
acc.print_info()
acc.set_percent(0.05)


# Изменение процента c использованием @property
# acc.percent = 0.05
acc.print_info()
