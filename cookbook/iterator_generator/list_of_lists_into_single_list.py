from collections import Iterable
from itertools import chain

"""You have a nested sequence that you want to flatten into a single list of values"""


def flatten(sequence, ignore_types=(str, bytes)):
    for item in sequence:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item


items = [1, 2, [3, 4, [5, 6], 7], 8]
names = ['Dave', 'Paula', ['Thomas', 'Lewis']]

for x in flatten(chain(items, names)):  # chain unites 2 sequences
    print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# Dave
# Paula
# Thomas
# Lewis
