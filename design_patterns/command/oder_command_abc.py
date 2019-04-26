from abc import ABCMeta, abstractmethod


class AbsOrderCommand(metaclass=ABCMeta):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass
