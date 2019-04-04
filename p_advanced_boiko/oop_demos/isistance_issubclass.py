a = 2
b = 'spam'
print(isinstance(a, int))  # True
print(isinstance(b, str))  # True

print(issubclass(bool, int))  # True; since bool is a subclass of int

a.mro()

