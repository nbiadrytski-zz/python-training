class Squares:
    """Define a user-defined iterable that generates squares on demand, instead of all at once"""

    def __init__(self, start, stop):
        self.value = start - 1  # decrement as self.value incremented in next as precondition
        self.stop = stop

    def __iter__(self):  # return iterator object which is self here
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


a = Squares(1, 5)
print(a.__dict__)  # {'value': 0, 'stop': 5}
for i in a:  # a can be iterated now as built-in (but only once)
    print(i, end=' ')  # 1 4 9 16 25

print('\n')

b = Squares(1, 5)
b_iter_obj = iter(b)  # iter calls __iter__
print(next(b_iter_obj))  # 1: next calls __next__
print(next(b_iter_obj))  # 4
print(next(b_iter_obj))  # 9
print(next(b_iter_obj))  # 16
print(next(b_iter_obj))  # 25
# print(next(b_iter_obj))  StopIteration raised

b = list(Squares(1, 5))  # when converted to list, b can be iterated multiple times
for i in b:
    print(i, end=' ')  # 1 4 9 16 25
print('\n')
for i in b:
    print(i, end=' ')  # 1 4 9 16 25


