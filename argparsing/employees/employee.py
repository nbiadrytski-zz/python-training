import logging


class Employee:

    def __init__(self, first_name, position):
        self.name = first_name
        self.position = position
        self.logger = logging.getLogger('main.argparsing.employees.Employee')
        self.logger.debug('Initialising CoffeeForMe owner')

    @property
    def fullname(self):
        return "{} {}".format(self.name, self.name[::-1].capitalize())

    def create_employee(self, args):
        print('Hi {}! You are the Owner of CoffeeForMe'.format(args.name[0]))
        self.logger.info('create_employee(): created Owner employee: {}'.format(self.__str__()))
        return Employee(args.name[0], args.position[0])

    def user_choice(self, choice_msg, delta):
        while True:
            try:
                choice_dict = dict()
                choice = int(input(choice_msg))
                value = choice
                self.logger.debug('Employee {} made a choice: {}'.format(self.__str__(), str(choice)))
            except ValueError:
                print('{}, you can input only numbers. Enter:'.format(self.name))
                print(' or '.join(str(x) for x in range(1, delta)) + '\n')
                continue
            if 0 < choice < delta:
                self.logger.debug('Employee {} choice "{}" is valid according to choice delta "{}"'.
                                  format(self.__str__(), str(choice), str(delta)))
                break
            else:
                print('{}, that is not:'.format(self.name))
                print(' or '.join(str(x) for x in range(1, delta)))
                print('Try again!\n')
        print('Your choice is {}\n'.format(choice))
        choice_dict[choice] = value
        return choice_dict[value]

    def view_records(self):
        print('Hi {}! Ask your managers if you need to see sales records'.format(self.fullname))

    def __str__(self):
        return '{} - {}'.format(self.name, self.position)


