# multi assignment
a = b = c = 1  # assign a, b, c a ref link to the same object (1) in memory
print(a is b)  # True
print(a is c)  # True; a refers to the same object as c
print(isinstance(a, int))  # True
c = 2
print(a is c)  # False; ref link is now different

# when you create a var, it is added to the dict (namespace) (where key is var name and value is ref link to object)
del a  # del keyword deletes key-value pair from that dict
# print(a)  NameError: name 'a' is not defined


x, y, z, = 1, 2, 'john'
print(x is y)  # False

# преобразование типа
f = 1
d = str(1)  # new object is created



