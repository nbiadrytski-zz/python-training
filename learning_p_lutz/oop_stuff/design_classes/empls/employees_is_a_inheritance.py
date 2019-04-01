class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return f'<Employee: name={self.name}, salary={self.salary}>'


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(f'{self.name} makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(f'{self.name} interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} makes pizza')


if __name__ == '__main__':

    bob = PizzaRobot('bob')
    print(bob)  # Run inherited __repr__; <Employee: name=bob, salary=50000>
    bob.work()  # bob makes pizza
    bob.give_raise(0.20)
    print(bob)  # <Employee: name=bob, salary=60000.0>

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
# Employee does stuff
# Chef makes food
# Server interfaces with customer
# PizzaRobot makes pizza
