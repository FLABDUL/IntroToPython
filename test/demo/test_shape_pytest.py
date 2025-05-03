import pytest

from src.demo.Shape import Circle, Rectangle, Shape


def test_rectangle_area():
    """
    Test the area calculation for a Rectangle.
    """
    rectangle = Rectangle(3, 4)
    assert rectangle.area() == 12  # Area = 3 * 4 = 12

def test_rectangle_perimeter():
    """
    Test the perimeter calculation for a Rectangle.
    """
    rectangle = Rectangle(3, 4)
    assert rectangle.perimeter() == 14  # Perimeter = 2 * (3 + 4) = 14

def test_circle_area():
    """
    Test the area calculation for a Circle.
    """
    circle = Circle(5)
    assert circle.area() == pytest.approx(3.1416 * 5 * 5, rel=1e-4)  # Area = π * r²

def test_circle_perimeter():
    """
    Test the perimeter calculation (circumference) for a Circle.
    """
    circle = Circle(5)
    assert circle.perimeter() == pytest.approx(2 * 3.1416 * 5, rel=1e-4)  # Perimeter = 2 * π * r

def test_invalid_shape_instantiation():
    """
    Test that we cannot instantiate an abstract class (Shape).
    """
    with pytest.raises(TypeError):
        Shape()  # Should raise an error because Shape is abstract
