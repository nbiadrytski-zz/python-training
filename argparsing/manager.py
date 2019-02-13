from argparsing.employee import Employee
from argparsing.db_funcs import *
from argparsing.functions import *


class Manager(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)

    def create_employee(self, args):
        print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
        print('You can view all sales records')
        return Manager(args.name[0], args.position[0])

    def view_records(self):
        try:
            employees = view_db_records()
            show_sales_table(employees)
            #export_as_json()
        except TypeError:
            print('\nNo sales records yet. Ask your salespeople to sell something...')
            # lod exception
