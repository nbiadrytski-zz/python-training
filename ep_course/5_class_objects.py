class A:
    number = 444  # class attribute

    # initialisation
    def __init__(self, value):  # self is the object of the class we we are working at the moment
        self.value = value

    def print_value(self):
        print(self.value)


print(A.number)  # 444

a = A('Hello!')  # <__main__.A object at 0x104798e48>
a.print_value()  # Hello!

print(a.number)  # 444
A.number = 42
print(a.number)  # 42

# dict of object attributes
print(a.__dict__)  # {'value': 'Hello!'}

print(A.__name__)  # A; class name
B = A
print(B.__name__)  # A

# add new class attribute
A.b = 'qwerty'
print(a.b)  # qwerty; a object now can access class attribute b

print(A.__bases__)  # (<class 'object'>,); list of parent classes
