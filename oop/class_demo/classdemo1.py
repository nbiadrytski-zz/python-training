class Car(object):  # object --> inheriting Object class

    # class member var
    wheels = 4

    def __init__(self, make, model):  # used to initialize all attributes; kind of Java constructor
        # When Car instance created, self will be used to refer to that instance
        self.make = make  # define make attribute
        self.model = model

    def info(self):
        print('Make of the car: ' + self.make)
        print('Model of the car: ' + self.model)


# created instance of Car class
# c1 a reference var that access instance in memory
c1 = Car('bmw', '550i')
c1.info()

# created another instance of Car class
c2 = Car('benz', 'E350')
c2.info()

print(Car.wheels)
