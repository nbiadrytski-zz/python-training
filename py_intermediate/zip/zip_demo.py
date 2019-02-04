x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a, b, c in zip(x, y, z):
    print(a, b, c)
print("="*32)

print(list(zip(x, y, z)))  # [(1, 7, 'a'), (2, 6, 'b'), (3, 2, 'c'), (4, 1, 'd')]
print("="*32)

print(dict(zip(x, z)))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print("="*32)

for i in zip(x, y, z):
    print(i)
print("="*32)

# list comprehension
[print(a, b, c) for a, b, c in zip(x, y, z)]
'''1 7 a
2 6 b
3 2 c
4 1 d'''

