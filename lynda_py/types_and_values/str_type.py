#!/usr/bin/env python3

x = 'seven'.capitalize()  # string is an object

y = 'seven {} {}'.format(8, 9).upper()  # positional args

n, m = 10, 11
d = f'digits {n:<9} {m}'  # f string, comes with python 3.6

print('x is {}'.format(x))
print('y is {}'.format(y))
print('d is {}'.format(d))

print(type(x))
