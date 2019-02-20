from unittest import TestCase
from argparsing.employees.salesperson import Salesperson
from argparsing.functions.db_funcs import *
from argparsing.functions.functions import *
from io import StringIO
from unittest.mock import patch
from unittest import mock
import random
import string
import shutil
import os


class SalespersonTest(TestCase):

    @staticmethod
    def create_salesperson(name='John'):
        return Salesperson(name, 'Salesperson', ['Tea'], ['Sugar'])

    @staticmethod
    def generate_random_name():
        name = ''.join(random.choices(string.ascii_letters, k=10))
        return name

    # def test_passed_args(self):
    #     parser = ArgumentParser.parse_arguments()
    #     args = parser.parse_args(['Nick', 'Salesperson', '-bev=Tea', '-add=Sugar'])
    #     self.assertEqual(args.name, ['Nick'])
    #     self.assertEqual(args.position, ['Salesperson'])
    #     self.assertEqual(args.beverage, ['Tea'])
    #     self.assertEqual(args.addition, ['Sugar'])

    def test_sp_employee_greeting(self):
        expected_output = 'Hi \x1b[32mJohn\x1b[0m! You are a Salesperson.Hello!\n'
        sp = SalespersonTest.create_salesperson()
        with patch('sys.stdout', new=StringIO()) as actual_output:
            sp.employee_greeting('Hello!')
            self.assertIn(expected_output, actual_output.getvalue(), '\n\nStrings do not match')

    def test_sp_fullname(self):
        sp = SalespersonTest.create_salesperson()
        full_name = sp.fullname
        self.assertEqual(full_name, 'John Nhoj', '\n\nStrings do not match')

    @mock.patch('argparsing.employees.employee.input', create=True)  # mocking user input
    def test_sp_user_choice_valid(self, mocked_input):
        sp = SalespersonTest.create_salesperson()
        mocked_input.side_effect = [1]
        choice = sp.user_choice('Input number:', 3)
        self.assertEqual(choice, 1)

    @mock.patch('argparsing.employees.employee.input', create=True)
    def test_sp_user_choice_exceed_delta(self, mocked_input):
        expected_output = 'John, that is not:\n1 or 2\nTry again!\n\nYour choice is 2\n\n'
        sp = SalespersonTest.create_salesperson()
        with patch('sys.stdout', new=StringIO()) as actual_output:
            mocked_input.side_effect = [11, 2]
            choice = sp.user_choice('Input number:', 3)
        self.assertIn(expected_output, actual_output.getvalue(), '\n\nStrings do not match')
        self.assertEqual(choice, 2)

    @mock.patch('argparsing.employees.employee.input', create=True)
    def test_sp_user_choice_invalid_type_passed(self, mocked_input):
        expected_output = 'John, you can input only numbers. Enter:\n1 or 2\n\nYour choice is 1\n\n'
        sp = SalespersonTest.create_salesperson()
        with patch('sys.stdout', new=StringIO()) as actual_output:
            mocked_input.side_effect = ['test', 1]
            choice = sp.user_choice('Input number:', 3)
        self.assertIn(expected_output, actual_output.getvalue(), '\n\nStrings do not match')
        self.assertEqual(choice, 1)

    @mock.patch('builtins.input', create=True)
    def test_sp_make_sale_beverage_only(self, mocked_input):
        name = SalespersonTest.generate_random_name()
        expected_output = 'Beverage: tea. Price: 4.0$\n'
        sp = SalespersonTest.create_salesperson(name)
        mocked_input.side_effect = [2, 'tea', 4]
        create_table()
        sp.make_sale(['Tea'], ['Sugar'])
        with open(employee_filename('salesperson_records', sp.fullname, '_records.txt'), 'r') as f:
            actual_output = f.read()
        self.assertTrue(is_employee_in_db(sp.fullname), '\nSalesperson is not found in db')
        self.assertEqual(expected_output, actual_output)

    @mock.patch('builtins.input', create=True)
    def test_sp_make_sale_beverage_and_addition(self, mocked_input):
        name = SalespersonTest.generate_random_name()
        expected_output = 'Beverage: tea. Price: 4.0$\nAddition: sugar. Price: 2.0$\n'
        sp = SalespersonTest.create_salesperson(name)
        mocked_input.side_effect = [1, 'tea', 4, 'sugar', 2]
        create_table()
        sp.make_sale(['Tea'], ['Sugar'])
        with open(employee_filename('salesperson_records', sp.fullname, '_records.txt'), 'r') as f:
            actual_output = f.read()
            self.assertTrue(is_employee_in_db(sp.fullname), '\nSalesperson is not found in db')
            self.assertEqual(expected_output, actual_output)

    @mock.patch('builtins.input', create=True)
    def test_sp_add_beverage(self, mocked_input):
        sp = SalespersonTest.create_salesperson()
        mocked_input.side_effect = ['cOfFeE', 2]
        record = sp.add_beverage(['Milk', 'Coffee'])
        self.assertEqual('Beverage: coffee. Price: 2.0$', record)

    @mock.patch('builtins.input', create=True)
    def test_sp_add_ingredient(self, mocked_input):
        sp = SalespersonTest.create_salesperson()
        mocked_input.side_effect = ['mIlK', 3]
        record = sp.add_ingredient(['Sugar', 'Milk'])
        self.assertEqual('Addition: milk. Price: 3.0$', record)

    def test_sp_total_sales_amount(self):
        sp = SalespersonTest.create_salesperson()
        with open(employee_filename('salesperson_records', sp.fullname, '_records.txt'), 'w') as f:
            f.write('Beverage: tea. Price: 4.0$\n')
            f.write('Beverage: water. Price: 4.3$\n')
            f.write('Addition: sugar. Price: 1.5$\n')
        total_amount = sp.total_sales_amount()
        self.assertEqual(9.8, total_amount)

    def test_sp_count_sales(self):
        sp = SalespersonTest.create_salesperson()
        with open(employee_filename('salesperson_records', sp.fullname, '_records.txt'), 'w') as f:
            f.write('Beverage: tea. Price: 4.0$\n')
            f.write('Beverage: water. Price: 4.3$\n')
            f.write('Addition: sugar. Price: 1.5$\n')
        sales_number = sp.count_sales()
        self.assertEqual(3, sales_number)

    def test_sp_view_records(self):
        sp = SalespersonTest.create_salesperson()
        expected_output = 'Beverage: tea. Price: 4.0$\n\nBeverage: water. Price: 4.3$\n\n' \
                          'Addition: sugar. Price: 1.5$\n\n'
        with open(employee_filename('salesperson_records', sp.fullname, '_records.txt'), 'w') as f:
            f.write('Beverage: tea. Price: 4.0$\n')
            f.write('Beverage: water. Price: 4.3$\n')
            f.write('Addition: sugar. Price: 1.5$\n')
        with patch('sys.stdout', new=StringIO()) as actual_output:
            sp.view_records()
            self.assertIn(expected_output, actual_output.getvalue(), '\n\nStrings do not match')

    def tearDown(self):
        try:
            folder_to_delete = os.path.join(os.path.dirname(__file__), 'salesperson_records')
            shutil.rmtree(folder_to_delete)
        except FileNotFoundError as e:
            print(e)
