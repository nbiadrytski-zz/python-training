import datetime


def decorator_func_with_args(arg1, arg2):
    def wrap(f):  # wrap() is used to wrap func1; f == func1
        print('1. Inside wrap()')

        def wrapped_f(*args): # actual replacement function
            print(f'3. Inside wrapped_f(): decorator args: {arg1}, {arg2}')
            print(f'4. Is about to __call__ {f}')
            before = time_check()
            f(*args)
            after = time_check()
            print(f'6. {f} was __called__ ')
            print(f'7. Elapsed time = {after - before}')
        return wrapped_f
    return wrap


def time_check():
    return datetime.datetime.now()


@decorator_func_with_args('test1', 'test2')
def func1(a1, a2, a3):  # this is actually wrapped_f() from decorator
    print(f'5. {func1} is being called with arguments: {a1}, {a2}, {a3}')


print('2. Finished decorating func1()')

func1('func1_arg1', 'func1_arg2', 'func1_arg3')
# 1. Inside wrap()
# 2. Finished decorating func1()
# 3. Inside wrapped_f(): decorator args: test1, test2
# 4. Is about to __call__ <function func1 at 0x102c46f28>
# 5. <function decorator_func_with_args.<locals>.wrap.<locals>.wrapped_f at 0x10307a950> is being called with arguments: func1_arg1, func1_arg2, func1_arg3
# 6. <function func1 at 0x102c46f28> was __called__
# 7. Elapsed time = 0:00:00.000014
