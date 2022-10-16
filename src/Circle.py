from src.Figure import Figure
from math import pi


# Создание класса Круг
class Circle(Figure):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    # Метод вычисления площади
    def get_area(self):
        area = round(pi * (self.radius ** 2))
        return area

    # Метод вычисления периметра
    def get_perimeter(self):
        perimeter = round(2 * pi * self.radius)
        return perimeter

