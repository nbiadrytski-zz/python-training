def class_tree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        class_tree(supercls, indent+3)


def instance_tree(inst):
    print(f'Tree of {inst}')
    class_tree(inst.__class__, 3)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d1 = D()

instance_tree(d1)
# ...D
# ......B
# .........A
# ............object
# ......C
# .........A
# ............object
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
