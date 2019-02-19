import argparse
import sys
import logging

logger = logging.getLogger('main.argparsing.argparser.argument_parser.ArgumentParser')


class ArgumentParser(argparse.ArgumentParser):
    """
    Parses positional and optional command-line arguments passed by user.
    ArgumentParser class inherits built-in argparse.ArgumentParser class.
    Overrides argparse.ArgumentParser error method to customize error for missing args.
    Prints -h for user when the app is started.
    """

    @staticmethod
    def parse_arguments():
        """
        Parses positional and optional command-line arguments passed by user.
        Prints -h for user when the app is started.
        Positional args: employee_name, employee_position.
        Optional args: beverage, addition

        Returns:
            argparse.Namespace: parsed arguments.
        """
        parser = ArgumentParser(description='Sell drinks and view sales records with "CoffeeForMe!"',
                                epilog='Thank you for using "CoffeeForMe" App!\n')

        parser.add_argument('name', type=str, nargs=1, metavar='employee_name', default=None,
                            help='Employee name')
        parser.add_argument('position', type=str, nargs=1, metavar='employee_position', default=None,
                            help='Employee position (Salesperson or Manager)')
        parser.add_argument('-bev', '--beverage', action='append', default=None,
                            help='List of available beverages a Salesperson can sell: tea, coffee, water, soda, etc.')
        parser.add_argument('-add', '--addition', action='append', default=None,
                            help='List of available ingredients a Salesperson can add: sugar, milk, cinnamon, etc.')

        parser.print_help()
        print('\n')

        args = parser.parse_args()

        logger.info('parse_arguments(): the following args were supplied by user: {}'.format(str(args)))

        return args

    def error(self, message):
        """
        Overrides argparse.ArgumentParser error method to customize error for missing args.
        Prints Help, message and exits.

        Parameters:
            message (str): message name.
        """
        logger.error('error(): obligatory args were not supplied bu user')
        self.print_help(sys.stderr)
        self.exit(0, '{} Error: {}'.format(self.prog, message))

    @staticmethod
    def quit_msg(name, position):
        """
        Prints info message with valid positions to user
        If invalid position was passed via command-line arguments.

        Parameters:
            name (str): Employee name.
            position (str): valid Employee position (Salesperson or Manager).
        """
        print('"{}" with "{}" position is not a valid employee'.format(name, position))
        print('Available positions: Salesperson or Manager')
