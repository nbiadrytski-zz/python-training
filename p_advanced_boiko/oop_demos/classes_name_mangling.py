class A:
    _atr1 = None
    __atr2 = None

    def prnt(self):
        print(self._atr1, self.__atr2)


a = A()
a.prnt()  # None None
# print(a.__attr2)  # AttributeError: 'A' object has no attribute '__attr2'

# BUT

a._A__atr2 = 'test'
a.prnt()  # None test
