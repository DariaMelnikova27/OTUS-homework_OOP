import pytest

from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

figure = Figure()
circle = Circle(23)
rectangle = Rectangle(25, 14)
square = Square(18)
triangle = Triangle(4, 6, 5)


class TestFigures:

    # Кейс 1. Проверка имени круга
    def test_circle_name(self):
        assert circle.name == 'Circle'

    # Кейс 2. Проверка имени прямоугольника
    def test_rectangle_name(self):
        assert rectangle.name == 'Rectangle'

    # Кейс 3. Проверка имени квадрата
    def test_square_name(self):
        assert square.name == 'Square'

    # Кейс 4. Проверка имени треугольника
    def test_triangle_name(self):
        assert triangle.name == 'Triangle'

    # Кейс 5. Проверка наличия у треугольника трех сторон, не равных 0
    def test_number_of_triangle_sides(self):
        assert triangle.side_a != 0 or triangle.side_b != 0 or triangle.side_c != 0

    # Кейс 6. Проверка корректного вычисления площади круга
    def test_circle_area(self):
        assert circle.get_area() == 1662

    # Кейс 7. Проверка корректного вычисления периметра круга
    def test_circle_perimeter(self):
        assert circle.get_perimeter() == 145

    # Кейс 8. Проверка корректного вычисления площади прямоугольника
    def test_rectangle_area(self):
        assert rectangle.get_area() == 350

    # Кейс 9. Проверка корректного вычисления периметра прямоугольника
    def test_rectangle_perimeter(self):
        assert rectangle.get_perimeter() == 78

    # Кейс 10. Проверка корректного вычисления площади квадрата
    def test_square_area(self):
        assert square.get_area() == 324

    # Кейс 11. Проверка корректного вычисления периметра квадрата
    def test_square_perimeter(self):
        assert square.get_perimeter() == 72

    # Кейс 12. Проверка корректного вычисления площади треугольника
    def test_triangle_area(self):
        assert triangle.get_area() == 10

    # Кейс 11. Проверка корректного вычисления периметра треугольника
    def test_triangle_perimeter(self):
        assert triangle.get_perimeter() == 15

    # Кейс 12. Проверка корректного вычисления суммы площадей двух фигур
    @pytest.mark.parametrize('figure', [circle, rectangle, square, triangle, 'qwerty', 123])
    @pytest.mark.parametrize('base_figure', [circle, rectangle, square, triangle])
    def test_add_area(self, figure, base_figure):
        if isinstance(figure, Figure):
            assert base_figure.add_area(figure) == figure.get_area() + base_figure.get_area()
        else:
            assert base_figure.add_area(figure) == 'Передан неверный класс геометрической фигуры'

