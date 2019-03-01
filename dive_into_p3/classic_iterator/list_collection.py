from dive_into_p3.classic_iterator.abstract_aggr_iter import Aggregate
from dive_into_p3.classic_iterator.list_iterator import ListIterator


class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)