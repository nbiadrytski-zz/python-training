class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value cannot be negative')
        instance.__dict__[self.name] = value

    # Called at the time the owning class owner is created. The descriptor has been assigned to name
    def __set_name__(self, owner, name):
        self.name = name


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 1, 10)
print(apple_order.total())  # 10

# apple_order.price = -10  # ValueError: Value cannot be negative

# apple_order.quantity = -10  # ValueError: Value cannot be negative
