from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract Base Class for different shapes.
    Forces any subclass to implement the area() and perimeter() methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of a rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle.
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate the area of a circle.
        """
        return 3.1416 * self.radius * self.radius

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of a circle.
        """
        return 2 * 3.1416 * self.radius


# Example usage
if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Circle(5)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} - Area: {shape.area()}, Perimeter: {shape.perimeter()}")
