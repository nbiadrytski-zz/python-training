from abc import ABCMeta, abstractmethod


class AbsStrategy(metaclass=ABCMeta):

    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost"""
