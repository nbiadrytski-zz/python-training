from argparsing.employee import Employee


class Manager(Employee):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def view_records(self):
        print('{} employed as {} is able to view records'.format(self.fullname, self.position))
