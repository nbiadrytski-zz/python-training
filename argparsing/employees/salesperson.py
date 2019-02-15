from argparsing.employees.employee import Employee
from argparsing.functions.db_funcs import *
from argparsing.functions.functions import *


class Salesperson(Employee):

    addition_msg = '''Would you like to add an ingredient to your beverage?
    1 - Add ingredient
    2 - Don not add ingredient\n'''

    def __init__(self, name, position, beverage):
        super().__init__(name, position)
        self.beverage = beverage

    def create_employee(self, args):
        print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
        print('You can sell the following beverages:')
        for beverage in args.beverage:
            print(Colors.GREEN + beverage + Colors.RESET)
        return Salesperson(args.name[0], args.position[0], args.beverage)

    @staticmethod
    def add_beverage(available_beverages):
        while True:
            print('You can sell the following beverages:')
            for beverage in available_beverages:
                print(Colors.GREEN + beverage + Colors.RESET)
            beverage_to_sell = input('Enter beverage name: \n')
            if beverage_to_sell.lower() in [x.lower() for x in available_beverages]:
                beverage_price = input('Enter beverage price: \n')
                sale_record = 'Beverage: {}. Price: {}$'.format(beverage_to_sell, str(beverage_price))
                return sale_record
            else:
                print('You can sell only:')
                print(' or '.join(Colors.RED + x + Colors.RESET for x in available_beverages))
                print(Colors.BLUE + 'Try again!' + Colors.RESET + '\n')

    @staticmethod
    def add_ingredient(available_additions):
        while True:
            print('You can add the following ingredients:')
            for addition in available_additions:
                print(Colors.GREEN + addition + Colors.RESET)
            addition_to_sell = input('Enter ingredient name: \n')
            if addition_to_sell.lower() in [addition.lower() for addition in available_additions]:
                addition_price = input('Enter ingredient price: \n')
                sale_record = 'Addition: {}. Price: {}$'.format(addition_to_sell, str(addition_price))
                return sale_record
            else:
                print('You can add only:')
                print(' or '.join(Colors.RED + addition + Colors.RESET for addition in available_additions))
                print(Colors.BLUE + 'Try again!' + Colors.RESET + '\n')

    def make_sale(self, available_beverages, available_additions):
        if self.user_choice(self.addition_msg, 3) == 2:
            beverage_to_file(employee_filename(self.fullname), self.add_beverage(available_beverages))
            if is_employee_in_db(self.fullname):
                update(self.fullname, self.count_sales(), self.total_sales_amount())
            else:
                insert(self.fullname, self.count_sales(), self.total_sales_amount())
        else:
            beverage_addition_to_file(employee_filename(self.fullname),
                                      self.add_beverage(available_beverages), self.add_ingredient(available_additions))
            if is_employee_in_db(self.fullname):
                update(self.fullname, self.count_sales(), self.total_sales_amount())
            else:
                insert(self.fullname, self.count_sales(), self.total_sales_amount())

    def total_sales_amount(self):
        try:
            with open(employee_filename(self.fullname), "r") as f:
                total_price = []
                for line in f:
                    try:
                        match_price(total_price, r'\d+', line)
                    except IndexError as e:
                        print('Sale price is missing in {} line --> {}'.format(line, e))
                print('Your sales total amount: {}$'.format(sum(total_price)))
                return sum(total_price)
        except TypeError as e:
            print('Invalid filename or no file passed... ', e)

    def count_sales(self):
        try:
            with open(employee_filename(self.fullname), 'r') as f:
                contents = f.read()
                beverage_counter = contents.count('Beverage')
                addition_counter = contents.count('Addition')
                print('You sold {} beverages and {} additions'.format(beverage_counter, addition_counter))
                return beverage_counter + addition_counter
        except TypeError as e:
            print('Invalid filename or no file passed... ', e)

    def view_records(self):
        try:
            with open(employee_filename(self.fullname), "r") as f:
                for line in f:
                    print(line)
        except TypeError as e:
            print('Invalid filename or no file passed... ', e)
