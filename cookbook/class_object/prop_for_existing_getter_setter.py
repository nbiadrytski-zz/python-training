"""Define property for existing get and set methods"""


class Tester:

    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, del_first_name)


p = Tester("Tom")
print(p.name)
p.name = "Jack"
print(p.name)
del p.name  # AttributeError: Can't delete attribute
