from .car import Car


class Electro_car(Car):
    def __init__(self, brend, model, year, probeg, battery):
        super().__init__(brend, model, year, probeg)
        self.battery = battery

    def get_info_2(self):
        return f"Этот автомобиль имеет мощность {self.battery}%"
