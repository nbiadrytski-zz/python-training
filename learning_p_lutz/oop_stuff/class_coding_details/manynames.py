X = 11  # Global (module) name/attribute (X, or manynames.X)


def f():
    print(X)  # Access global X (11)


def g():
    X = 22  # Local (function) variable (X, hides module X)
    print(X)


class C:
    X = 33  # Class attribute (C.X)

    def m(self):
        X = 44  # Local variable in method (X)
        self.X = 55  # Instance attribute (instance.X)


if __name__ == '__main__':
    print(X)  # 11; file (module) X global var (line 1)
    f()  # 11; printing file (module) X global var from line 1
    g()  # 22; printing function g() local var defined in line 9

    obj = C()
    print(obj.X)  # 33; printing class attr X defined in line 14
    obj.m()  # attach self.X to obj now
    print(obj.X)  # 55; Instance attribute from line 18
    print(C.X)  # 33; Class attribute (C.X) stays unchanged
