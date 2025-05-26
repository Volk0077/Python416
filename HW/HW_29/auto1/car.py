class Car:
    def __init__(self, brend, model, year, probeg):
        self.brend = brend
        self.model = model
        self.year = year
        self.probeg = probeg

    def get_info(self):
        return f"{self.brend}, {self.model}, {self.year} год, {self.probeg} км"
