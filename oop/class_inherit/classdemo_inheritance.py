class Car(object):
    def __init__(self):
        print("You just created Car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")


class BMW(Car):
    def __init__(self):
        super().__init__()  # Car.__init__(self)
        print("You just created BMW instance")

    def drive(self):
        super(BMW, self).drive()  # super().drive()
        print("You are driving BMW")

    def headup_display(self):
        print("This is a unique feature")


# c = Car()
# c.drive()
# c.stop()

b = BMW()
b.drive()
b.stop()
b.headup_display()
