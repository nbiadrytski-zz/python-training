class LittleMeta(type):

    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        attributedict['LittleMeta_attribute_name'] = f'LittleMeta attribute value in {clsname}'
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class S:
    pass


class A(S, metaclass=LittleMeta):
    pass


class B(S, metaclass=LittleMeta):
    pass


a = A()
# clsname:  A
# superclasses:  (<class '__main__.S'>,)
# attributedict:  {'__module__': '__main__', '__qualname__': 'A', 'LittleMeta_attribute_name': 'LittleMeta attribute value in A'}

b = B()
# clsname:  B
# superclasses:  (<class '__main__.S'>,)
# attributedict:  {'__module__': '__main__', '__qualname__': 'B', 'LittleMeta_attribute_name': 'LittleMeta attribute value in B'}

print(a.LittleMeta_attribute_name)  # LittleMeta attribute value in A
print(b.LittleMeta_attribute_name)  # LittleMeta attribute value in B
