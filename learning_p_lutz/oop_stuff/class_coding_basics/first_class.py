class FirstClass:
    def set_data(self, value):
        self.data = value

    def display_data(self):
        print(self.data)


class SecondClass(FirstClass):
    def display_data(self):
        print(f'Current data: {self.data}')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):  # is run when a ThirdClass instance appears in a + expression
        return ThirdClass(self.data + other)

    def __str__(self):  # is run when an object is printed
        return f'[ThirdClass: {self.data}]'

    def mul(self, other):
        self.data *= other


def upper_name(obj):
    return obj.data.upper()


# at this point, we have three objects: two instances and a class
x = FirstClass()
y = FirstClass()

x.set_data('King Arthur')
y.set_data(3.14159)  # same as FirstClass.set_data(y, 3.14159)

x.display_data()
y.display_data()  # same as FirstClass.display_data(y)

x.data = 'New Value'
x.display_data()  # New Value

x.anothername = 'spam'
print(x.anothername)  # spam; generate an entirely new attribute in the instance’s namespace

sc = SecondClass()
sc.set_data(42)
sc.display_data()  # Current data: 42

a = ThirdClass('abc')
a.display_data()  # Current data: abc
print(a)  # [ThirdClass: abc]
b = a + 'xyz'  # __add__: makes a new instance
b.display_data()  # Current data: abcxyz
print(b)  # [ThirdClass: abcxyz]
a.mul(3)  # mul: changes instance in place
print(a)  # [ThirdClass: abcabcabc]

namespace = list(name for name in a.__dict__ if not name.startswith('__'))
print(namespace)  # ['data']

print(a.__class__)  # <class '__main__.ThirdClass'>

print(upper_name(x))  # NEW VALUE

