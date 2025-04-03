from math import pi

area = {
    "Circle": lambda x: pi * x * x,
    "Rectangle": lambda x, y: x * y,
    "Trapezoid": lambda a, b, h: (a + b) * h / 2,
}

print(area["Circle"](2))
print(area["Rectangle"](10, 13))
print(area["Trapezoid"](7, 5, 3))
