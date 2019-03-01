from dive_into_p3.classic_iterator.abstract_aggr_iter import Iterator


class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        """
        :param collection: list
        :param cursor: start index.
        also check -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Cursor start index -1.
        Because first of all we need to call next()
        which will move cursor to 1.
        """
        self._cursor = -1

    def next(self):
        """
        If cursor points to last element, the call StopIteration,
        else move cursor to 1
        """
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        """
        Return current element
        """
        return self._collection[self._cursor]