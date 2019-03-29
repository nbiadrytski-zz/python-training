class Iters:

    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):  # used for indexing and slicing
        return self.data[item]

    def __iter__(self):  # used for iteration
        print(f'__iter__ over Iters instance with value {self.data}:')
        for x in self.data:
            yield x

    def __contains__(self, item):  # membership
        print(f'Does Iters instance with value {self.data} contain {item}?')
        return item in self.data


X = Iters([1, 2, 3, 4, 5])
print(3 in X)
# Does Iters instance with value [1, 2, 3, 4, 5] contain 3?
# True

for i in X:
    print(i, end=' | ')
# __iter__ over Iters instance with value [1, 2, 3, 4, 5]:
# 1 | 2 | 3 | 4 | 5 |
print()

print([i ** 2 for i in X])
# __iter__ over Iters instance with value [1, 2, 3, 4, 5]:
# [1, 4, 9, 16, 25]

print(list(map(bin, X)))
# __iter__ over Iters instance with value [1, 2, 3, 4, 5]:
# ['0b1', '0b10', '0b11', '0b100', '0b101']

print(X[:])  # [1, 2, 3, 4, 5]; will fail without __getitem__

