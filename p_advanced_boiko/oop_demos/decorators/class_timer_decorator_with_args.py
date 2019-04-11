class TimerDecoratorWithArgsClass:

    def __init__(self, before, after):
        """
        If there are decorator arguments, the function to be decorated is not passed to the constructor
        """
        print('1. Inside __init__()')
        self.before = before
        self.after = after

    def __call__(self, f):  # the function to be decorated is passed to __call__
        print(f'2. Function object {f} created in __call__() method.')

        def wrapped_f(*args):
            import datetime
            print(f'4. Is about to __call__ {f}')
            self.before = datetime.datetime.now()
            f(*args)
            self.after = datetime.datetime.now()
            print(f'6. {f} was __called__ ')
            print(f'7. Elapsed time = {self.after - self.before}')
        return wrapped_f


@TimerDecoratorWithArgsClass('before', 'after')
def func1(a1, a2, a3, a4):
    print(f'5. func1() is being called with arguments: {a1}, {a2}, {a3}, {a4}')


print('3. Finished decorating func1()')

func1('func1_arg1', 'func1_arg2', 'func1_arg3', 'func1_arg4')
# 1. Inside __init__()
# 2. Function object <function func1 at 0x109509400> created in __call__() method.
# 3. Finished decorating func1()
# 4. Is about to __call__ <function func1 at 0x109509400>
# 5. func1() is being called with arguments: func1_arg1, func1_arg2, func1_arg3, func1_arg4
# 6. <function func1 at 0x109509400> was __called__
# 7. Elapsed time = 0:00:00.000013
