x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')


class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'

    def __str__(self):  # default
        return f'str: the number of bunnies is {self._n}'


x = Bunny(42)
print(x)  # str: the number of bunnies is 42
print(repr(x))  # repr: the number of bunnies is 42

print(chr(128406))  # 🖖

print(ord('🖖'))  # 128406
