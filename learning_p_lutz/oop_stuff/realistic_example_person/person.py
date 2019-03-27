class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name  # self is the new instance object
        self.job = job  # self.name, self.job, self.pay are instance attributes
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):  # print object info
        return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':  # run below only when the file is run for testing, not when the file is imported.
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)  # [Person: Bob Smith, 0]
    print(sue)  # [Person: Sue Jones, 100000]
    print(bob.last_name(), sue.last_name())  # Smith Jones
    sue.give_raise(.10)
    print(sue)  # [Person: Sue Jones, 110000]

    tom = Manager('Tom Jones', 'mgr', 50000)
    tom.give_raise(.10)  # Jones
    print(tom.last_name())
    print(tom)  # [Person: Tom Jones, 60000]

    print('--All three--')
    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)
# [Person: Bob Smith, 0]
# [Person: Sue Jones, 121000]
# [Person: Tom Jones, 72000]
