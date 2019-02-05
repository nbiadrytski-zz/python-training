#!/usr/bin/env python3


x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)

print('x is {}'.format(x))
print(type(x))  # <class 'tuple'>
print(type(x[0]))  # <class 'int'>

print(id(x))  # 4359340632 unique id for each object

print(id(x[0]))  # 4458535536 same as id(y[0])
print(id(y[0]))  # 4458535536

if x[0] is y[0]:
    print("x[0] and y[0] is the same object")
else:
    print("x[0] and y[0] are NOT the same object")

if x is y:
    print("x and y is the same object")
else:
    print("x and y are NOT the same object")


if isinstance(x, tuple):
    print('x is a tuple')
else:
    print('x is not a tuple')