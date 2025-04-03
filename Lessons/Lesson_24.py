# Продолжение ООП ____________________________________


# Задача: реализовать класс "Человек"

'''
class Human:
    name = "name"
    birthday = "00.00.0000"
    phone = "00-00-00"
    country = "country"
    city = "city"
    address = "street, house"

    def print_info(self):
        print(" Персональные данные ".center(40, "*"))
        print(f"Имя: {self.name}")
        print(f"Дата рождения: {self.birthday}")
        print(f"Номер телефона: {self.phone}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Адрес: {self.address}")
        print("=" * 40)

    def input_info(self, first_name, birthday, phone, country, city, address):
        self.name = first_name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):# Устанавливаем новое имя
        self.name = name

    def get_name(self):# Получаем имя 
        return self.name


h1 = Human()
h1.print_info()
h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Бульвар")
h1.print_info()
h1.set_name('Юлия')
h1.print_info()
print(h1.get_name())
'''

#Задача создать класс Person с данными о сотруднике (имя, фамилия) и двумя методами

class Person:
    skill = 10
    
    def __init__(self,  name, surname):# инициализатор, отрабатывает в момент создания экземпляра класса
        self.name = name
        self.surname = surname

    def __del__(self): # разрывает ссылку на экземпляр класса 
        print("Удаление экземпляра")

    def print_info(self):
        print("Данные сотрудника:", self.name, self.surname)

    def add_skill(self, k):
        self.skill += k
        print('Квалификация сотрудника:', self.skill)


p1 = Person("Виктор", "Резник")
p1.print_info()
p1.add_skill(3)

del p1

p2 = Person("Анна", "Долгих")
p2.print_info()
p2.add_skill(2)