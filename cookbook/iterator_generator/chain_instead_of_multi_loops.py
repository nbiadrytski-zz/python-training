from itertools import chain

"""
You need to perform the same operation on many objects, but the objects are contained
in different containers, and you’d like to avoid nested loops without losing the readability
of your code.
"""

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

# 1
# 2
# 3
# 4
# x
# y
# z
