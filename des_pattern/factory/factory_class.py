from math import sin, cos


class Point:
    """
    You cannot make multiple constructors in Python. And making if statement in __init__
    is not the best idea as well. But you can use factory methods to create different objects of Point class.
    Here factory methods are in separate class PointFactory.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


# take out factory methods to a separate class
class PointFactory:

    def new_cartesian_point0(self, x, y):  # can used to save object state
        p = Point(x, y)
        return p

    @staticmethod  # factory method
    def new_cartesian_point1(x, y):
        return Point(x, y)

    @staticmethod  # factory method
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    p_init = Point(2, 3)
    p_static_method1 = PointFactory.new_cartesian_point1(3, 4)
    p_static_method2 = PointFactory.new_polar_point(1, 2)
    print(p_init)
    print(p_static_method1)
    print(p_static_method2)

    pf = PointFactory()
    p3 = PointFactory.new_cartesian_point0(pf, 1, 2)
    print(p3)