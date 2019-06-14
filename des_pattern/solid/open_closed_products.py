from enum import Enum
from abc import ABCMeta, abstractmethod


# Open Closed:
# A class should be open for extension (usually by inheritance), but closed for modification
# which means it's not a good idea to change smth that is already properly working,
# but it's better to extend the functionality in a new class


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Enterprise patterns: Specification (inheritance)
class Spec(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied(self, item):
        """Does an item satisfy the requirement?"""
        pass


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, items, spec):
        pass


class ColorSpec(Spec):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpec(Spec):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class CombinedSpec(Spec):
    def __init__(self, spec1, spec2):
        self.spec2 = spec2
        self.spec1 = spec1

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


class ProductFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)
products = [apple, tree, house]

prod_filter = ProductFilter()

print('Green products:')
green = ColorSpec(Color.GREEN)
for p in prod_filter.filter(products, green):
    print(f' - {p.name} is green')

print('Large products:')
large = SizeSpec(Size.LARGE)
for p in prod_filter.filter(products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
large_blue = CombinedSpec(large, ColorSpec(Color.BLUE))
for p in prod_filter.filter(products, large_blue):
    print(f' - {p.name} is large and blue')
