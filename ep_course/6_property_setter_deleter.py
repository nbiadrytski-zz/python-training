class Foo:
    def __init__(self):
        self._bar = 0

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value + 1

    @bar.deleter
    def bar(self):
        del self._bar


f = Foo()
print(f.bar)
f.bar = 5
print(f.bar)