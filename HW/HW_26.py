class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def show(self):
        print(f"{self.name}", end=" ")
        self.laptop.show()

    class Laptop:
        def __init__(self, model="HP", cpu="I7", memory="16"):
            self.model = model
            self.cpu = cpu
            self.memory = memory

        def show(self):
            print(f"=> {self.model}, {self.cpu}, {self.memory}")


name1 = Student("Roman")
name1.show()

name2 = Student("Vlad")
name2.show()
