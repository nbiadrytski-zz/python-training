class CompareObjects:
    """
    We want our person objects to be equal if all their attributes have the same values,
    and we want to be able to order them alphabetically by surname and then by first name.
    """

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __eq__(self, other):  # does self == other?
        return self.name == other.name and self.surname == other.surname

    def __gt__(self, other):  # is self > other?
        if self.surname == other.surname:
            return self.name > other.name
        return self.surname > other.surname

    # now we can define all the other methods in terms of the first two

    def __ne__(self, other):  # does self != other?
        return not self == other  # calls self.__eq__(other)

    def __le__(self, other):  # is self <= other?
        return not self > other  # this calls self.__gt__(other)

    def __lt__(self, other):  # is self < other?
        return not (self > other or self == other)

    def __ge__(self, other):  # is self >= other?
        return not self < other


obj1 = CompareObjects('Mike', 'Smith')
obj2 = CompareObjects('Mike', 'Smith')
obj3 = CompareObjects('Alice', 'Brown')


print(obj1.__eq__(obj2))  # True; Mike Smith == Mike Smith
print(obj1.__eq__(obj3))  # False; Mike Smith != Alice Brown

print(obj1.__gt__(obj2))  # False; Mike Smith is not greater than
print(obj1.__gt__(obj3))  # True; Smith is greater than Brown

print(obj1.__ne__(obj2))  # False; Mike Smith == Mike Smith
print(obj1.__ne__(obj3))  # True; Mike Smith != Alice Brown
