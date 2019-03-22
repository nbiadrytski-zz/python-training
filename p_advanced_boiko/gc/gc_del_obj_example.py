import sys
import gc


class Class1:
    def __del__(self):  # is called on object when garbage collector destroys it
        print(f'{self.__class__.__name__} deleted')


class Class2:
    def __del__(self):
        print(f'{self.__class__.__name__} deleted')


def f():
    a = Class1()
    b = Class2()
    #del a
    print(f'a refs count: {sys.getrefcount(a)}, b refs count: {sys.getrefcount(b)}\n')  # a refs count: 2, b refs count: 2

f()

print('END')
