class C:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f'C({self.x})'

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x


c1 = C(1)
c2 = C(1)

# create empty dict which will hold custom C objects where its key is C instance
custom_dict = dict()  # as c1 == c2 and dict keys should be unique, so just one C instance will be added to dict
custom_dict[c1] = 'this_is_c1'
custom_dict[c2] = 'this_is_c2'
print(custom_dict)  # {C(1): 'this_is_c2'}

# set is container of hashable unique objects
# as c1 == c2, so just one C instance will be added to set
custom_set = set()
custom_set.add(c1)
custom_set.add(c1)
print(custom_set)  # {C(1)}
