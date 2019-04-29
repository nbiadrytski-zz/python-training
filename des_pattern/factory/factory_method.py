from math import sin, cos


class Point:
    """
    You cannot make multiple constructors in Python. And making if statement in __init__
    is not the best idea as well. But you can use factory methods to create different objects of Point class
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod  # factory method
    def new_cartesian_point1(x, y):
        return Point(x, y)

    @classmethod  # factory method
    def new_cartesian_point2(cls, x, y):
        return cls(x, y)

    @staticmethod  # factory method
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    p_init = Point(2, 3)
    p_static_method = Point.new_cartesian_point1(3, 4)
    p_class_method = Point.new_cartesian_point2(3, 4)
    p_static_method2 = Point.new_polar_point(1, 2)
    print(p_init)
    print(p_static_method)
    print(p_class_method)
    print(p_static_method2)
