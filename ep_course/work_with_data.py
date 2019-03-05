# multi assignment
a = b = c = 1  # assign a, b, c share the same ref link to the same object (1) in memory
print(a is b)  # True
print(a is c)  # True; a refers to the same object as c
print(isinstance(a, int))  # True
c = 2
print(a is c)  # False; ref link is now different

# when you create a var, it is added to the dict (namespace) (where key is var name and value is ref link to object)
del a  # del keyword deletes key-value pair from that dict
# print(a)  NameError: name 'a' is not defined


x, y, z, = 1, 2, 'john'
print(x is y)  # False

# преобразование типа
f = 1
d = str(1)  # new object is created

# immutable - int, float, str, tuple
g = 'foo'
t = g  # t and g point to the same object
print(g)  # foo
t += 'bar'
print(g)  # foo

# mutable - list, dict, object
x1 = [1, 2, 3]
y1 = x1  # y1 and x1 point to the same object
print(x1)  # [1, 2, 3]
y1 += [4, 5, 6]
print(x1)  # [1, 2, 3, 4, 5, 6]

# in      not in
# is object in collection? (list, tuple, dict)
print(2 in x1)  # True
print(1 not in x1)  # False

# is       is not
# compare by ref link
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True
print(list1 is list2)  # False; list1 and list2 are different objects

b1 = 'test'  # or 1
c1 = 'test'  # or 1
print(b1 is c1)  # True; share the same link to the same immutable object

# multiply list elements
from functools import reduce
print(reduce(lambda x3, y3: x3*y3, [1, 2, 3]))  # 6

res = 1
for item in [1, 2, 3]:
    res *= item
print(res)  # 6




