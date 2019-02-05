a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if a and b:
    print('a and b expression is true')
else:
    print('a and b expression is false')


if a or b:
    print('a or b expression is true')
else:
    print('a or b expression is false')

if not b:
    print('not b expression is true')
else:
    print('not b expression is false')

if y in x:
    print('y in x expression is true')
else:
    print('y in x expression is false')

if 'tree' in x:
    print('tree in x expression is true')
else:
    print('tree in x expression is false')

if y is x[0]:
    print('y is x[0] expression is true')
else:
    print('y is x[0] expression is false')

if y is not x[1]:
    print('y is not x[1] expression is true')
else:
    print('y is not x[1] expression is false')