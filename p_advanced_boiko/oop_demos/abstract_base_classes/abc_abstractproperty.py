from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    def __init__(self):
        self._x = 1
        self.base_attrib = 'base_attrib_value'

    @property
    @abstractmethod
    def x(self):
        return self._x

    @x.setter
    @abstractmethod
    def x(self, value):
        self._x = value

    @x.deleter
    @abstractmethod
    def x(self):
        del self._x


class Impl(Base):
    def __init__(self):
        super().__init__()  # same as Base.__init__(self)
        self.impl_atttib = 'impl_attrib_value'

    @property
    def x(self):
        print('Impl getter called...')
        return self._x

    @x.setter
    def x(self, value):
        print('Impl setter called...')
        self._x = value + 1

    @x.deleter
    def x(self):
        print('Impl deleter called...')
        del self._x


impl = Impl()
print(impl.x)  # Impl getter called..., 1
impl.x = 7  # Impl setter called...
print(impl.x)  # Impl getter called..., 8
print(impl.base_attrib)  # base_attrib_value
print(impl.impl_atttib)  # impl_attrib_value
del impl.x  # Impl deleter called...




