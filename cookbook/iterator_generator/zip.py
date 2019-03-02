from itertools import zip_longest

xpts = [1, 5, 4]
ypts = [101, 78]

# Iteration stops whenever one of the input sequences is exhausted
for x, y in zip(xpts, ypts):
    print(x, y)  # tuple

# 1 101
# 5 78

# puts None for non-matching value
for item in zip_longest(xpts, ypts):
    print(item)

# (1, 101)
# (5, 78)
# (4, None)

for item in zip_longest(xpts, ypts, fillvalue='I am Not Real!'):
    print(item)

# (1, 101)
# (5, 78)
# (4, 'I am Not Real!')

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

# (1, 10, 'x')
# (2, 11, 'y')
# (3, 12, 'z')
print('=='*32)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)  # {'name': 'ACME', 'shares': 100, 'price': 490.1}

for name, val in zip(headers, values):
    print(name, '=', val)

# name = ACME
# shares = 100
# price = 490.1

