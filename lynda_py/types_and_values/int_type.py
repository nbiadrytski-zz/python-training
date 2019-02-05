#!/usr/bin/env python3
from decimal import *

x = 8 * 2
y = 7 * 3.124
z = 7 / 3
n = 7 // 3

# used for money counting
a = Decimal('3.10')  # 10 cents
b = Decimal('.30')  # 30 cents
c = a + a + a + a - b


print('x is {}'.format(x))  # x is 16
print('y is {}'.format(y))  # y is 21.868000000000002
print('z is {}'.format(z))  # z is 2.3333333333333335
print('n is {}'.format(n))  # n is 2
print('с is {}'.format(c))


print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'float'>
print(type(n))  # <class 'int'>
print(type(c))  # <class 'decimal.Decimal'>
