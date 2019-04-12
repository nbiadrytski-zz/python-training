from collections.abc import Set


class MyListBasedSet(Set):
    """
    Providing custom Set implementation based on given list using collections.abc module.
    A set object is an unordered collection of distinct hashable objects.
    """
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return f'{self.elements}'


s1 = MyListBasedSet([0, 1, 2, 1, 3])
s2 = MyListBasedSet([3, 4, 5])

print(s1)  # [0, 1, 2, 3]; duplicate 1 is removed as it is a set
print(len(s1))  # 4; 4 elements, not 5
print(s1 & s2)  # 3; 3 is a common element in s1 and s2
print(1 in s1)  # True
print(s1.isdisjoint(s2))  # False; Return True if the set has no elements in common with other: 3 is in common
print(s1 | s2)  # [0, 1, 2, 3, 4, 5]; return new set with the elements from s1 and elements from s2 which are not in s1
