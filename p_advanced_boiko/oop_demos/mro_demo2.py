from learning_p_lutz.oop_stuff.design_classes.mix_ins.listinstance import ListInstance


class G: pass


class F(G): pass


class E(G): pass


class D(G): pass


class C(E): pass


class B(D, E, F): pass


class A(ListInstance, B, C):
    def __init__(self, name):
        self.name = name


print(A.mro())
# [<class '__main__.A'>, <class 'learning_p_lutz.oop_stuff.design_classes.mix_ins.listinstance.ListInstance'>,
# <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.F'>,
# <class '__main__.G'>, <class 'object'>]

b = A('Bob')
print(b)
# <Instance of A, address 4337516104:
# 	name=Bob
# >
