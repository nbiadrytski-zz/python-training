from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    @abstractmethod
    def method(self):
        print('Base.method()')


class Impl(Base):

    def method(self):
        print('Impl.method()')
        super(Impl, self).method()  # same as Base.method(self)


inst = Impl()
inst.method()
# Impl.method
# Base.method()
