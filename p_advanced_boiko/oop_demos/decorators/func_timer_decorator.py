def func_timer_decorator(f):
    def new_f():  # new_f() is created and returned when func_timer_decorator() is called
        import datetime
        before = datetime.datetime.now()
        print(f'1. Is about to call {f}')
        f()
        after = datetime.datetime.now()
        print(f'3. Just called {f}')
        print(f'4. Elapsed time = {after - before}')
    return new_f


@func_timer_decorator  # same as func1 = func_timer_decorator(func1)
def func1():
    print('2. inside func1()')


func1()
print(func1.__name__)  # new_f; because new_f function has been substituted for the original function during decoration
# 1. Is about to call <function func1 at 0x1062d4400>
# 2. inside func1()
# 3. Just called <function func1 at 0x1062d4400>
# 4. Elapsed time = 0:00:00.000077
