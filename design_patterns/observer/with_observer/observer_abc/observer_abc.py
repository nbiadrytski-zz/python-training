from abc import ABCMeta, abstractmethod


class AbsObserver(metaclass=ABCMeta):

    @abstractmethod
    def update(self, value):
        pass

    # add __enter__ and __exit__ to create a context manager
    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass