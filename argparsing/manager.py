from argparsing.employee import Employee


class Manager(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)

    def create_employee(self, args):
        print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
        print('You can view sales records')
        return Manager(args.name[0], args.position[0])

    def view_records(self):
        print('{} employed as {} is able to view records'.format(self.fullname, self.position))
