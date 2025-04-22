class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def show_rect(self):
        print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")


class RectFon(Rect):
    def __init__(self, width, height, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()
        print("Фон:", self.fon)


# Домашка-----------------------------------------------------------------------------------------------
class RectBorder(Rect):
    def __init__(self, width, height, frame_width, frame_type, frame_color):
        super().__init__(width, height)
        self.frame_width = frame_width
        self.frame_type = frame_type
        self.frame_color = frame_color

    def show_rect(self):
        super().show_rect()
        print(
            f"Ширина рамки: {self.frame_width}\nТип рамки: {self.frame_type}\nЦвет рамки: {self.frame_color}"
        )


shape1 = RectFon(400, 200, "yellow")
shape1.show_rect()
# # Домашка-----------------------------------------------------------------------------------------------
shape2 = RectBorder(600, 300, "1px", "solid", "blue")
shape2.show_rect()
