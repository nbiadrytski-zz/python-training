class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):  # instance method
        return f'{self.name} {self.surname}'

    @property
    def fullname_property(self):  # instance method
        return f'{self.name} {self.surname}'

    @classmethod
    def allowed_titles_starting_with(cls, startswith):
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith):
        return [t for t in Person.TITLES if t.endswith(endswith)]


jane = Person('Jane', 'Smith')

print(jane.fullname())
print(jane.fullname_property)

print(Person.allowed_titles_starting_with('M'))
print(Person.allowed_titles_ending_with('s'))

print(jane.allowed_titles_starting_with('M'))
print(jane.allowed_titles_ending_with('s'))