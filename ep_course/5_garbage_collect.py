import sys


class A:
    """Check how many ref links the object has"""
    pass


x = A()  # 1 ref
y = x  # 2 refs
l = [x, ]  # 3 refs

print(sys.getrefcount(x))  # 4; getrefcount creates additional local ref link to x, that's why 4

del x
print(sys.getrefcount(y))  # 3 refs
del y
print(sys.getrefcount(l))  # 2 refs
del l


# garbage collector works by counting ref links
# if object's ref links count becomes 0, then object is deleted
# GC looks for objects whose ref links refer to each other and decreases these links




