class Metacls(type):
    # name -- name of the class we want to create
    # bases -- parent classes of the class we want to create
    # dict -- adding new 'meta' attr to the class we want to create
    def __new__(mcls, name, bases, dict):
        dict['meta'] = f'{name}, metacls was here'
        return type.__new__(mcls, name, bases, dict)


class A(metaclass=Metacls):
    pass


class B(metaclass=Metacls):
    pass


a = A()
print(a.meta)
b = B()
print(b.meta)