from learning_p_lutz.oop_stuff.design_classes.empls.employees_is_a_inheritance import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f'{self.name} orders from {server}')

    def pay(self, server):
        print(f'{self.name} pays for item to {server}')


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    """container and controller;
    its constructor makes and embeds instances of the employee classes
    """
    def __init__(self):
        self.server = Server('Pat Server')  # Embed Server object
        self.chef = PizzaRobot('Teddy Robot')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)  # activate Customer
        customer.order(self.server)  # # Customer orders from server initialised in PizzaShop.__init__
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == "__main__":

    scene = PizzaShop()  # Make the composite
    scene.order('Homer')  # Simulate Homer's order
    # Homer orders from < Employee: name = Pat Server, salary = 40000 >
    # Teddy Robot makes pizza
    # oven bakes
    # Homer pays for item to <Employee: name=Pat Server, salary=40000>
    print('...')

    scene.order('Shaggy')  # Simulate Shaggy's order
    # Shaggy orders from <Employee: name=Pat Server, salary=40000>
    # Teddy Robot makes pizza
    # oven bakes
    # Shaggy pays for item to <Employee: name=Pat Server, salary=40000>

