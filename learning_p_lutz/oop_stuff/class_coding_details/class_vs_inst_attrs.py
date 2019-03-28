class MixedNames:

    data = 'spam'  # class attr

    def __init__(self, value):
        self.data = value  # instance attr

    def display(self):  # display() is also class attr --> inherited by every instance made from the class
        print(f'self.data = {self.data}, MixedNames.data = {MixedNames.data}')


x = MixedNames(1)
y = MixedNames(2)

x.display()
y.display()
# self.data = 1, MixedNames.data = spam
# self.data = 2, MixedNames.data = spam
