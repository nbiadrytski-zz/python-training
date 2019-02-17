import argparse
import sys


class ArgumentParser(argparse.ArgumentParser):

    @staticmethod
    def parse_arguments():
        parser = ArgumentParser(description="Buy drinks and view records with Coffee App!",
                                prog='Coffee CLI App-->',
                                epilog='Thank you for using Coffee CLI App!')

        parser.add_argument('name', type=str, nargs=1, metavar='employee_name', default=None,
                            help='Employee name')
        parser.add_argument('position', type=str, nargs=1, metavar='employee_position', default=None,
                            help='Employee position')
        parser.add_argument("-bev", "--beverage", action='append', default=None,
                            help="List of available beverages: tea, coffee, water, soda, milk, etc.")
        parser.add_argument("-add", "--addition", action='append', default=None,
                            help="List of available beverage additions: sugar, milk, cinnamon, etc. ")

        args = parser.parse_args()
        return args

    # overriding ArgumentParser error method to customize error for missing args
    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(0, '{} Error: {}'.format(self.prog, message))

    @staticmethod
    def quit_msg(name, position):
        print('"{}" with "{}" position is not a valid employee'.format(name, position))
        print('Available positions: Salesperson or Manager')

