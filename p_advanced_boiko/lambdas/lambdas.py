def make_incrementor(n):  # we define a function which returns another function
    return lambda x: x + n  # returns anonymous func


f = make_incrementor(3)
print(type(f))  # <class 'function'>, f это прибавляльщик числа 3 к чему-нибудь
print(f(3))  # 6
print(f(4))  # 7


action = (lambda x: (lambda y: x + y))  # nested lambda
act = action(99)
print(act(3))  # 103

