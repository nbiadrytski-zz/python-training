def f1(func):
    def f2():
        print('this is f2() before func call')
        func()
        print('this is f2() after func call')
    return f2


@f1
def f3():
    print('this is f3()')


f3()
