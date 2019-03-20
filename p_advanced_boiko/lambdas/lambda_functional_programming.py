from functools import reduce

foo = [1, 2, 3]
bar = [0, 2, 0]

y = filter(lambda x: x % 3 == 0, foo)  # takes each item from iterable (foo) and applies predicate (lambda) to it
for i in y:
    print(i)
print(type(y))  # <class 'filter'>
# 3

z = map(lambda n, m: n * m, foo, bar)  # map lambda action to items from iterables foo and bar
for item in z:
    print(item)
print(type(z))  # <class 'map'>
# 0
# 4
# 0

v = reduce(lambda a, b: a + b, foo)  # sum all foo elems; reducing foo elems to one result
print(v)  # 45
print(type(v))  # <class 'int'>
