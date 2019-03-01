from dive_into_p3.classic_iterator.list_collection import ListCollection

collection = (1, 2, 5, 6, 8)
aggregate = ListCollection(collection)
itr = aggregate.iterator()

while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())