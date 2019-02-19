from unittest import TestCase
from argparsing.argsparser.argument_parser import ArgumentParser
from argparsing.employees.salesperson import Salesperson
from io import StringIO
from unittest.mock import patch

# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/argparsing/tests/test_salesperson.py


class SalespersonTest(TestCase):

    def test_passed_args(self):
        parser = ArgumentParser.parse_arguments()
        args = parser.parse_args(['Nick', 'Salesperson', '-bev=Tea', '-add=Sugar'])
        self.assertEqual(args.name, ['Nick'])
        self.assertEqual(args.position, ['Salesperson'])
        self.assertEqual(args.beverage, ['Tea'])
        self.assertEqual(args.addition, ['Sugar'])

    def test_salesperson_creation(self):
        parser = ArgumentParser.parse_arguments()
        args = parser.parse_args(['Nick', 'Salesperson', '-bev=Tea', '-add=Sugar'])
        salesperson = Salesperson(args.name[0], args.position[0], args.beverage, args.addition)
        self.assertEqual(salesperson.name, 'Nick')
        self.assertEqual(salesperson.position, 'Salesperson')
        self.assertEqual(salesperson.beverage, ['Tea'])
        self.assertEqual(salesperson.addition, ['Sugar'])

    def test_salesperson_create_employee(self):
        parser = ArgumentParser.parse_arguments()
        args = parser.parse_args(['Nick', 'Salesperson', '-bev=Tea', '-add=Sugar'])
        salesperson = Salesperson(args.name[0], args.position[0], args.beverage, args.addition)
        s = salesperson.create_employee(args)
        self.assertEqual(s.name, 'Nick')
        self.assertEqual(s.position, 'Salesperson')
        self.assertEqual(s.beverage, ['Tea'])
        self.assertEqual(s.addition, ['Sugar'])

    def test_salesperson_create_employee_console_output(self):
        with patch('sys.stdout', new=StringIO()) as output:
            print_output = 'usage: _jb_unittest_runner.py [-h] [-bev BEVERAGE] [-add ADDITION]' \
                   '\n                              employee_name employee_position\n\nSell drinks and view sales ' \
                   'records with "CoffeeForMe!"\n\npositional arguments:\n  employee_name         ' \
                   'Employee name\n  employee_position     Employee position (Salesperson or Manager)\n\n' \
                   'optional arguments:\n  -h, --help            show this help message and exit\n  -bev BEVERAGE' \
                   ', --beverage BEVERAGE\n                        List of available beverages a Salesperson' \
                   ' can sell:\n                        tea, coffee, water, soda, etc.\n  -add ADDITION,' \
                   ' --addition ADDITION\n                        List of available ingredients' \
                   ' a Salesperson can add:\n                        sugar, milk, cinnamon, etc.' \
                   '\n\nThank you for using "CoffeeForMe" App!\n\n\nHi \x1b[32mNick\x1b' \
                   '[0m! You are a Salesperson.\nYou can sell the following beverages:\n\x1b[32mTea\x1b[0m\n'
            parser = ArgumentParser.parse_arguments()
            args = parser.parse_args(['Nick', 'Salesperson', '-bev=Tea', '-add=Sugar'])
            salesperson = Salesperson(args.name[0], args.position[0], args.beverage, args.addition)
            salesperson.create_employee(args)
            self.assertIn(print_output, output.getvalue(), '\n\nStrings do not match')


