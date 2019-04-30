import copy


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


john = Person("John", Address("123 London Road", "London", "UK"))
print(john)

jane = copy.deepcopy(john)  # making a new object that does not refer to the original john
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print(john, '\n', jane)
