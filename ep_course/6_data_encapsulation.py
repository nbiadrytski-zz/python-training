class JustCounter:
    __secret_count = 0

    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)


class A:
    bar = 1
    _bar = 2  # name convention: attribute should not be used outside class
    __bar = 3  # vip attribute, do not use outside class
    __bar__ = 4  # name convention: kind of magic attributes


counter = JustCounter()
counter.count()  # 1
counter.count()  # 2
print(counter._JustCounter__secret_count)  # 2

a = A()
print(a.bar)  # 1
print(a._bar)  # 2
print(a.__bar__)  # 4
# print(a.__bar)  AttributeError: 'A' object has no attribute '__bar'
# BUT
print(a._A__bar)  # 3
