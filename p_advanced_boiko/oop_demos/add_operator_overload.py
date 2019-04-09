class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):  # used when in print(), __repr__ used when in interpreter
        return f'Vector {self.a}, {self.b}'

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(7, 9)
v2 = Vector(2, -30)

print(v1 + v2)  # Vector 9, -21
