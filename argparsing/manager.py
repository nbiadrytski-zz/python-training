from argparsing.employee import Employee
from argparsing.db_funcs import *
from argparsing.functions import *


class Manager(Employee):

    manager_export_msg = '''Would you like to export sales records? Enter 1, 2, 3 or 4:
        1 - Export as JSON
        2 - Export as XML
        3 - Export as CSV
        4 - Do not export\n'''

    def __init__(self, name, position):
        super().__init__(name, position)

    def create_employee(self, args):
        print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
        print('You can view all sales records\n')
        return Manager(args.name[0], args.position[0])

    def view_records(self):
        try:
            employees = view_db_records()
            show_sales_table(employees)
        except TypeError:
            print('\nNo sales records yet. Ask your salespeople to sell something...')
            # lod exception

    def export_records(self):
        choice = self.user_choice(self.manager_export_msg, 5)
        if choice == 1:
            print('export json')
            export_as_json((self.fullname + '_records.json'))
        elif choice == 2:
            print('export xml')
            export_as_xml(self.fullname + '_records.xml')
        elif choice == 3:
            print('export csv')
            export_as_csv(self.fullname + '_records.csv')
        elif choice == 4:
            print('do not export')




