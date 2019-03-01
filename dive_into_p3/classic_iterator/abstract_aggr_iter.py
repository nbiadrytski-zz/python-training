import abc


class Aggregate(abc.ABC):
    def iterator(self):
        """
        Returns iterator
        """
        pass


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        """
        Returns iterator to the beginning of Aggregate.
        Same as reset.
        """
        pass

    @abc.abstractmethod
    def next(self):
        """
        Goes to the next element of aggregate.
        Raises StopIteration when the end of iteration is achieved.
        """
        pass

    @abc.abstractmethod
    def current(self):
        """
        Returns current element.
        """
        pass

