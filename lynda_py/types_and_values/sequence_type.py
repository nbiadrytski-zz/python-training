#!/usr/bin/env python3


x = [1, 2, 3, 4, 5]
x[2] = 42
for i in x:
    print('i is {}'.format(i))

print('='*32)

y = (1, 2, 3, 4, 5)
for i in y:
    print('i is {}'.format(i))

print('='*32)

z = range(5, 30, 5)  # 3rd param 5 is step
for i in z:
    print('i is {}'.format(i))

print('='*32)

c = list(range(9))
c[2] = 42
for i in c:
    print('i is {}'.format(i))

print('='*32)

v = {'one': 1, 'two': 2, 'three': 3}
v['three'] = 42
for k, v in v.items():
    print('k: {}, v: {}'.format(k, v))
