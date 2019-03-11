class Ancestor:
    def __init__(self):
        print('Ancestor.__init__')


class Child1(Ancestor):
    def __init__(self):
        print("Child1.__init__")
        super().__init__()


class Child2(Ancestor):
    def __init__(self):
        print("Child2.__init__")
        super().__init__()


class Child3(Child1, Child2):
    def __init__(self):
        print("Child3.__init__")
        super().__init__()


# class Child4(Child3, Child1, Child2):
#     def __init__(self):
#         print("Child4.__init__")
#         super().__init__()


c = Child3()
# Algorythm: linerisation method
# Child3.__init__
# Child1.__init__
# Child2.__init__
# Ancestor.__init__


print(Child3.mro())
# [<class '__main__.Child3'>, <class '__main__.Child1'>, <class '__main__.Child2'>, <class '__main__.Ancestor'>, <class 'object'>]