# Создание базового класса геометрической фигуры


class Figure:
    area = None

    # Метод вычисления площади (переопределен в классах-наследниках)
    def get_area(self):
        pass

    # Метод, который принимает другую геометрическую фигуру и возвращает сумму площадей этих фигур
    def add_area(self, figure):
        if isinstance(figure, Figure):
            sum_areas = figure.get_area() + self.get_area()
            return sum_areas
        else:
            raise ValueError("Передана не геометрическая фигура")

