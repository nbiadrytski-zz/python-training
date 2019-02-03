class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        #  return "Pair __repr__({}, {})".format(self.x, self.y)
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):  # __str__ is called by default when printing instance
        # return "Pair __str__({}, {})".format(self.x, self.y)
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(p)
print(p.__repr__())
