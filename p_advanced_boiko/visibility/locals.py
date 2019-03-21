q = lambda: locals()  # dict of local vars
print(q())  # {}


def d(b):
    a = 1
    print(locals()) # locals --> {'a': 1, 'b': 2}
    print(globals())
# globals -->
# {'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10e6928d0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': '/path/to/current/file.py', '__cached__': None,
# 'q': <function <lambda> at 0x10e61bea0>, 'd': <function d at 0x10e7eb488>}


d(2)
