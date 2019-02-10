from argparsing.employee import Employee
from argparsing.functions import *
import re


class Salesperson(Employee):

    addition_msg = 'Would you like to add an ingredient to your beverage?\n 1 - Add addition\n 2 - Don not add addition'

    def __init__(self, name, position, beverage):
        super().__init__(name, position)
        self.beverage = beverage

    def create_employee(self, args):
        print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
        print('You can sell the following beverages: {}'.format(args.beverage))
        return Salesperson(args.name[0], args.position[0], args.beverage)

    def make_sale(self, available_beverages, available_additions):
        if ask_user(self.addition_msg) == 'no':
            beverage_to_file(employee_filename(self.fullname), add_beverage(available_beverages))
        else:
            beverage_addition_to_file(employee_filename(self.fullname),
                                      add_beverage(available_beverages), add_ingredient(available_additions))

    def total_sales_amount(self):
        try:
            with open(employee_filename(self.fullname), "r") as f:
                total_price = []
                for line in f:
                    try:
                        result = re.findall(r'\d+', line)
                        price = int(result[0])
                        total_price.append(price)
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






