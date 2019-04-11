class PropertyViaDecorator:

    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property"""
        print('...getter called...')
        return self._x

    @x.setter
    def x(self, value):
        print('...setter called...')
        self._x = value

    @x.deleter
    def x(self):
        print('...deleter called...')
        del self._x


prop = PropertyViaDecorator()

print(prop._x)  # None
print(prop.x)  # ...getter called...  None

prop.x = 13  # ...setter called...
print(prop._x)  # 13
print(prop.x)  # ...getter called...   None

del prop.x  # ...deleter called...
