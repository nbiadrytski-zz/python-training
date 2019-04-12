from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    @abstractmethod
    def load(self, input):
        return

    @abstractmethod
    def save(self, output, data):
        return


class C(Base):
    pass

# b = Base() # TypeError: Can't instantiate abstract class Base with abstract methods load, save
# c = C()  # TypeError: Can't instantiate abstract class C with abstract methods load, save




