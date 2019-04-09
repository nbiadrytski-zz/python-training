class Symbol:

    def __init__(self, value):
        self.value = value

    def is_this_none(self):
        if self.value is None:
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        if self.is_this_none():
            return 'this_is_none'
        else:
            return str(self.value)


if __name__ == '__main__':

    x = Symbol('NP')
    y = Symbol('NP')

    # symbols_set = set()  # create set and add Symbol custom objects to it
    # symbols_set.add(x)
    # symbols_set.add(y)
    # print(len(symbols_set))  # 1

    symbols_dict = {x: x, y: y}  # create dict where values are Symbol custom objects
    print(symbols_dict)  # {1: <__main__.Symbol object at 0x10fb64400>, 2: <__main__.Symbol object at 0x10fb64438>}

    print(x is y)  # False
    print(x == y)  # True


