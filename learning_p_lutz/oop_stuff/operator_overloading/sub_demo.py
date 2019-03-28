class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)  # Result is a new instance

    def __add__(self, other):
        return Number(self.data + other)


X = Number(5)
Y = X - 2
print(Y.data)  # 3
Z = Y + 20
print(Z.data)  # 23

