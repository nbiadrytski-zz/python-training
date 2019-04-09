class Names:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f'Getting name: {self._name}'

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            print(f'Setting name to {value}')
            self._name = value
        else:
            raise TypeError('name must be a string !!!')

    @name.deleter
    def name(self):
        print('Deleting name ...')
        del self._name


person = Names('Bob')

print(person.name)  # Getting name: Bob

person.name = 'John'  # Setting name to John
print(person.name)  # Getting name: John

del person.name  # Deleting name ...
