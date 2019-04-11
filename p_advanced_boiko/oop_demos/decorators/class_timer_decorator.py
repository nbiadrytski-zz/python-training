class TimerDecoratorClass:

    def __init__(self, f):  # create function object and later use it in the __call__() method
        self.f = f
        print(f'1. Function object {self.f} created in __init__ method, but not called yet.')

    def __call__(self):
        import datetime
        before = datetime.datetime.now()
        print(f'3. Is about to __call__ {self.f}')
        self.f()
        after = datetime.datetime.now()
        print(f'5. Just finished the __call__ of {self.f}')
        print(f'6. Elapsed time = {after-before}')


# same as:
# tdc = TimerDecoratorClass(func1)
# tdc.__call__()
@TimerDecoratorClass
def func1():
    print("4. inside func1()")


print("2. Finished decorating func1()")

func1()

# 1. Function object <function func1 at 0x10c431e18> created in __init__ method, but not called yet.
# 2. Finished decorating func1()
# 3. Is about to __call__ <function func1 at 0x10c431e18>
# 4. inside func1()
# 5. Just finished the __call__ of <function func1 at 0x10c431e18>
# 6. Elapsed time = 0:00:00.000040

