from src.Figure import Figure


# Создание класса Квадрат
class Square(Figure):
    def __init__(self, side_a):
        self.name = "Square"
        self.side_a = side_a

    # Метод вычисления площади
    def get_area(self):
        area = self.side_a ** 2
        return area

    # Метод вычисления периметра
    def get_perimeter(self):
        perimeter = 4 * self.side_a
        return perimeter

