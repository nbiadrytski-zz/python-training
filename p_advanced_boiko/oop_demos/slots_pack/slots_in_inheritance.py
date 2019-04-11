from sys import getsizeof


class Base:
    __slots__ = 'foo', 'bar'


class Correct(Base):  # inherited 'foo', 'bar' from Base
    __slots__ = 'baz',


class Wrong(Base):  # no need to redefine 'foo', 'bar' as they are inherited from Base
    __slots__ = 'foo', 'bar', 'baz'


print(dir(Correct))  # [..., 'bar', 'baz', 'foo']

print(getsizeof(Base()))  # 56
print(getsizeof(Correct()))  # 64
# Wrong is bigger, though has the same slots as Correct
print(getsizeof(Wrong()))  # 80
