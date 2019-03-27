from learning_p_lutz.oop_stuff.realistic_example_person.persontools import AttrDisplay


class Person(AttrDisplay):
    """
    Create and process person records.
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name  # self is the new instance object
        self.job = job  # self.name, self.job, self.pay are instance attributes
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':  # run below only when the file is run for testing, not when the file is imported.
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)

    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)
