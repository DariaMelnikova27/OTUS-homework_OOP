import math
from src.Figure import Figure


# Создание класса Треугольник
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.name = "Triangle"
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if side_a == 0 or side_b == 0 or side_c == 0:
            raise ValueError()

    # Метод вычисления площади
    def get_area(self):
        half_perimeter = self.get_perimeter() * 0.5
        area = round(math.sqrt(half_perimeter *
                               (half_perimeter - self.side_a) *
                               (half_perimeter - self.side_b) *
                               (half_perimeter - self.side_c)))

        return area

    # Метод вычисления периметра
    def get_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

