class C:
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x


c1 = C(1)
c2 = C(1)
print(c1 == c2)  # True
print(hash(c1))  # 1
