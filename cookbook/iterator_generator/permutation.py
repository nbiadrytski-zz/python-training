import itertools


items = ['a', 'b', 'c']

for p in itertools.permutations(items):
    print(p)

# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')