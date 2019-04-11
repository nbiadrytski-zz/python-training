class PropertyInfo:

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    # helps to hide kind of private var _x
    x = property(getx, setx, delx, '"x" property docstring')


prop = PropertyInfo()

print(prop.x)  # None
prop.x = 30
print(prop.x)  # 30
print(prop._x)  # 30

