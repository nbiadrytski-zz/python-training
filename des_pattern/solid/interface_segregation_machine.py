from abc import abstractmethod, ABCMeta

# bad
# class Machine:
#     def print(self, document):
#         raise NotImplementedError()
#
#     def fax(self, document):
#         raise NotImplementedError()
#
#     def scan(self, document):
#         raise NotImplementedError()


class Printer(metaclass=ABCMeta):
    @abstractmethod
    def print(self, document): pass


class Scanner(metaclass=ABCMeta):
    @abstractmethod
    def scan(self, document): pass


class Faxer(metaclass=ABCMeta):
    @abstractmethod
    def fax(self, document): pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful
