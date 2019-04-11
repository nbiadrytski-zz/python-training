class TimerDecoratorWithoutArgsClass:

    def __init__(self, f):  # init is called only once, though func1 called twice
        self.f = f
        print(f'1. Function object {self.f} created in __init__ method, but not called yet.')

    def __call__(self, *args):  # __call__() is called every time you call the decorated func1()
        import datetime
        before = datetime.datetime.now()
        print(f'3. Is about to __call__ {self.f}')
        self.f(*args)
        after = datetime.datetime.now()
        print(f'5. Just finished the __call__ of {self.f}')
        print(f'6. Elapsed time = {after - before}')


@TimerDecoratorWithoutArgsClass  # no arguments
def func1(a1, a2, a3, a4):
    print(f'4. func1 args: {a1}, {a2}, {a3}, {a4}')


print('2. Finished decorating func1()')

func1('1', '2', '3', '4')
func1('1', '2', '3', '4')
# 1. Function object <function func1 at 0x10ffb1e18> created in __init__ method, but not called yet.
# 2. Finished decorating func1()
# 3. Is about to __call__ <function func1 at 0x10ffb1e18>
# 4. func1 args: 1, 2, 3, 4
# 5. Just finished the __call__ of <function func1 at 0x10ffb1e18>
# 6. Elapsed time = 0:00:00.000030
# 3. Is about to __call__ <function func1 at 0x10ffb1e18>
# 4. func1 args: 1, 2, 3, 4
# 5. Just finished the __call__ of <function func1 at 0x10ffb1e18>
# 6. Elapsed time = 0:00:00.000013
