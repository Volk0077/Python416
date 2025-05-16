from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @abstractmethod
    def info(self):
        print(f"\n{self.surname} {self.name} {self.age}", end=" ")


class Student(Human):
    def __init__(self, name, surname, age, speciality, groups, rating):
        super().__init__(name, surname, age)
        self.speciality = speciality
        self.groups = groups
        self.rating = rating

    def info(self):
        super().info()
        print(f"{self.speciality} {self.groups} {self.rating}", end=" ")


class Teacher(Human):
    def __init__(self, name, surname, age, subject, experience):
        super().__init__(name, surname, age)
        self.subject = subject
        self.experience = experience

    def info(self):
        super().info()
        print(f"{self.subject} {self.experience}", end=" ")


class Graduate(Student):
    def __init__(self, name, surname, age, speciality, groups, rating, topic):
        super().__init__(name, surname, age, speciality, groups, rating)
        self.topic = topic

    def info(self):
        super().info()
        print(f"{self.topic}")


group = [
    Student("Даши", "Батодалаев", 16, "ГК", "Web_011", 5),
    Student("Линар", "Загидуллин", 32, "РПО", "PD_011", 5),
    Teacher("Андрей", "Даньшин", 38, "Астрофизика", 110),
    Graduate("Сергей", "Шугани", 15, "PПО", "PD_011", 5,
            "Защита персональных данных")
]

for i in group:
    i.info()


# Функторы

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(self.count)


c1 = Counter()
c1()
c1()
c1()

def string_strip(chars):
    def wrap(string):
        if not isinstance(string, str):
            raise ValueError("Аргумент должен быть строкой")

        return string.strip(chars)

    return wrap


s1 = string_strip("?:!.; ")
print(s1("   Hello World!  ...  "))


class StringStrip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        if not isinstance(string, str):
            raise ValueError("Аргумент должен быть строкой")

        return string.strip(self.chars)


s2 = StringStrip("?:!.; ")
print(s2("   Hello World!  ...  "))