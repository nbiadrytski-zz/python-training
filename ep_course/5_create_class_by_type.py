# create class with Type func

X = type('X', (object,), dict(a=1))  # name, parent class, attributes

x = X()
print(x.a)