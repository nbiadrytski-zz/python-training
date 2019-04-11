class MetaCls(type):
    def __call__(cls, *largs, **kwargs):
        new = cls.__new__(cls, *largs, **kwargs)
        new.meta = cls.__name__, 'MetaCls was here'
        if isinstance(new, cls):
            new.__init__(*largs, **kwargs)
        return new


class Cls(metaclass=MetaCls):
    def __init__(self):
        print(self.meta)


Cls()  # ('Cls', 'MetaCls was here')
