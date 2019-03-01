import abc


class Shape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        """Area calculation"""
        pass


class Rectangle(Shape):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


rectangle = Rectangle(10, 5)
triangle = Triangle(10, 5)

print(f'Rectangle area: {rectangle.area()}')
print(f'Triangle area: {triangle.area()}')
