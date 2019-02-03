class A:
    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2


a = A()
print(a.x)

b = B()
print(b.y)
