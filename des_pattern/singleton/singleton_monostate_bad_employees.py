# all members are static :)


class CEO:  # prevent people from creating new instances of CEO
    __shared_state = {'name': 'Steve', 'age': 55}

    def __init__(self):
        # whenever you initialise CEO you always refer to the same set of attributes
        self.__dict__ = self.__shared_state  # assign your set of attributes to __shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'


if __name__ == '__main__':
    # ceo1 = CEO()
    # print(ceo1)  # Steve is 55 years old
    #
    # ceo2 = CEO()
    # ceo2.age = 77
    # ceo2.name = 'Tim'
    # print(ceo1)
    # print(ceo2)

    cfo1 = CFO()
    cfo1.name = 'Sheryl'
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep='\n')

# Sheryl manages $1
# Ruth manages $10
# Ruth manages $10
