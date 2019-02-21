from unittest import TestCase
from argparsing.functions.functions import *
from argparsing.argsparser.argument_parser import ArgumentParser
import shutil


class FunctionsTest(TestCase):

    def setUp(self):
        self.parser = ArgumentParser.parse_arguments()

    def tearDown(self):
        # delete temp folder and files created by tests
        try:
            salesperson_records_tmp_folder = os.path.join(os.path.dirname(__file__), 'manager_records')
            shutil.rmtree(salesperson_records_tmp_folder)
        except FileNotFoundError as e:
            print(e)

    def test_get_employee_position_salesperson(self):
        args = self.parser.parse_args(['John', 'SaLeSpErSoN'])
        pos = get_employee_position(args)
        self.assertEqual('salesperson', pos)

    def test_get_employee_position_manager(self):
        args = self.parser.parse_args(['John', 'mAnaGeR'])
        pos = get_employee_position(args)
        self.assertEqual('manager', pos)

    def test_get_employee_position_invalid_pos(self):
        args = self.parser.parse_args(['John', 'Seller'])
        pos = get_employee_position(args)
        self.assertEqual(None, pos)

    def test_employee_filename(self):
        file_path = employee_filename('manager_records', 'Mike Jones', '_file.txt')
        self.assertEqual('manager_records/Mike Jones_file.txt', file_path)
