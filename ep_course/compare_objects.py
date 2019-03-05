a = 1
b = 1
print(a == b)  # True
print(b is a)  # True; share the same ref link to the same immutable object

c = d = 'test'
print(c == d)  # True
print(c is d)  # True

e = [1, 2, 3]
f = [1, 2, 3]
print(e == f)  # True; values are equal
print(e is f)  # False; 2 different objects, ref links are different
print(help(e))


