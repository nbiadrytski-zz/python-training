l = [1, 2, 3]


def append_to_l(l):  # l will be cjanged
    l.append(42)


def my_mult(number1, number2: int) -> int:  # type hints
    return number1 * number2


def my_func(number1, number2, number3):
    print(number1, number2, number3)


def my_func2(number=12):
    print(number)


def my_func3(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)


def my_func4(a, b, c, *args, **kwargs):
    print('a: ', a)
    print('b: ', b)
    print('c: ', c)
    print('args: ', args)
    print('kwargs: ', kwargs)


append_to_l(l)
print(l)  # [1, 2, 3, 42]

my_func(1, 2, 3)  # 1 2 3
my_func(number2=2, number1=1, number3=3)  # 1 2 3

my_func2()  # 12

my_func3(1, 2, 3, 'test', value='qwerty')
# args:  (1, 2, 3, 'test')
# kwargs:  {'value': 'qwerty'}

print('---------')
my_func4(1, 2, 3, 4, 'test', **{'kwargs': 'kw value'})
# a:  1
# b:  2
# c:  3
# args:  (4, 'test')
# kwargs:  {'kwargs': 'kw value'}

my_func4(1, 2, 3, 'test', **{'kwargs': 'kw value'}, **{'kwargs2': 'kw value2'})
# a:  1
# b:  2
# c:  3
# args:  ('test',)
# kwargs:  {'kwargs': 'kw value', 'kwargs2': 'kw value2'}
print('---------')

