#!/usr/bin/env python3


x = True
y = 7 < 5
z = None

if z:
    print('z is True')
else:
    print('z is False')  # z is False

print('x is {}'.format(x))  # x is True
print('y is {}'.format(y))  # y is False
print('z is {}'.format(z))  # z is None


print(type(x))  # <class 'bool'>
print(type(y))  # <class 'bool'>
print(type(z))  # <class 'NoneType'>
