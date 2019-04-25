from abc import ABCMeta, abstractmethod


class MyABC(metaclass=ABCMeta):
    """Abstract Base Class Definition"""

    @abstractmethod
    def do_something(self, value):
        """Required method"""

    @property
    @abstractmethod
    def some_property(self):
        """Required property"""


class MyClass(MyABC):
    """Implementation of MyABC"""

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop


a = MyClass(value=42)
print(a.some_property)
a.do_something(value=41)
print(a.some_property)




