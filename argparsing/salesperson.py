from argparsing.employee import Employee


class Salesperson(Employee):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def make_sale(self):
        print('{} employed as {} is able to create a sale'.format(self.fullname, self.position))
