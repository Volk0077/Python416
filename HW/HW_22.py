class Car:
    model = "X7 M50i"
    year = "2021"
    manufacturer = "BMW"
    engine_power = "530 л.с."
    color = "white"
    price = "10790000"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(
            f"Название модели: {self.model}\nГод выпуска: {self.year}\n"
            f"Производитель: {self.manufacturer}\nМощность двигателя: {self.engine_power}\n"
            f"Цвет машины: {self.color}\nЦена: {self.price}"
        )
        print("=" * 40)

    def input_info(self, model, year, manufacturer, engine_power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def set_model(self, model):  # устанавливаем новое имя
        self.model = model

    def get_model(self):  # получаем имя
        return self.model


h1 = Car()
h1.print_info()
# h1.input_info("X5", "2020", "BMW", "200 л.с.", "black", "50000")
# h1.print_info()
# h1.set_model("X3")
# print(h1.get_model())
