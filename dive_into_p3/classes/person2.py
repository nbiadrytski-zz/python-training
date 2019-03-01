class Person2:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, value):
        name, surname = value.split(" ", 1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname
        print('deleting fn')


jane = Person2("Jane", "Smith")
print(jane.fullname)  # @property

jane.fullname = "Jane Doe"  # @fullname.setter
print(jane.fullname)  # @property

del jane.fullname  # @fullname.deleter
