class Employee:

    def __init__(self, first_name, position):
        self.name = first_name
        self.position = position

    @property
    def fullname(self):
        return "{} {}".format(self.name, self.name[::-1].capitalize())

    def create_employee(self, args):
        print('Hi {}! You are the Owner of CoffeeForMe'.format(args.name[0]))
        return Employee(args.name[0], args.position[0])

    def view_records(self):
        print('Hi {}! Ask your managers if you need to see sales records'.format(self.fullname))





