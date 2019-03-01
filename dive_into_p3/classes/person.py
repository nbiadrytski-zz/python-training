class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')  # Class attribute: shared by all instances

    def __init__(self, title, name, surname):
        if title not in self.TITLES:  # TITLES is available as a property on the instance object
            raise ValueError(f'{title} is not a valid title')
        self.name = name  # attribute
        self.surname = surname  # attribute

    def fullname(self):  # instance method
        return f'{self.name} {self.surname}'

    @property
    def fullname_property(self):
        return f'{self.name} {self.surname}'

    # class method still has its calling object as the first parameter cls
    # If we call class method from an instance, this parameter will contain the instance object
    # if we call it from the class it will contain the class object
    @classmethod
    def allowed_titles_starting_with(cls, startswith):
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith):
        return [t for t in Person.TITLES if t.endswith(endswith)]


jane = Person('Mrs', 'Jane', 'Smith')
print(Person.TITLES)  # ('Dr', 'Mr', 'Mrs', 'Ms'); can be accessed via class name
print(jane.TITLES)  # ('Dr', 'Mr', 'Mrs', 'Ms'); can be accessed from class instance as well

print(jane.fullname())  # Jane Smith; calling instance method
print(jane.fullname_property)  # Jane Smith; calling property

print(Person.allowed_titles_starting_with('M'))  # ['Mr', 'Mrs', 'Ms']; calling class method via class name
print(jane.allowed_titles_starting_with('M'))  # ['Mr', 'Mrs', 'Ms']; calling class method via instance object

print(Person.allowed_titles_ending_with('s'))  # ['Mrs', 'Ms']; calling static method via class name
print(jane.allowed_titles_ending_with('s'))  # ['Mrs', 'Ms']; calling static method via instance object
