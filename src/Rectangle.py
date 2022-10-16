from src.Figure import Figure


# Создание класса Прямоугольник
class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.name = "Rectangle"
        self.side_a = side_a
        self.side_b = side_b

    # Метод вычисления площади
    def get_area(self):
        area = self.side_a * self.side_b
        return area

    # Метод вычисления периметра
    def get_perimeter(self):
        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

