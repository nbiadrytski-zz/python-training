"""Customize access to an attribute by defining it as a “property.”"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete an attribute")


p = Person("Mikalai")

print(p.name)  # calling getter: Mikalai
p.name = "Nick"
print(p.name)  # calling setter: Nick
del p.name  # AttributeError: Can't delete an attribute


