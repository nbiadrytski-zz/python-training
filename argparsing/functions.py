from argparsing.colors import Colors


def is_manager(args):
    if args.position[0].lower() == 'manager':
        return True


def is_salesperson(args):
    if args.position[0].lower() == 'salesperson':
        return True


def employee_filename(fullname):
    file_name = fullname + '_records.txt'
    return file_name


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


def beverage_to_file(file_name, beverage_record='Default beverage'):
    with open(file_name, "a") as f:
        f.write(beverage_record + "\n")


def beverage_addition_to_file(file_name, beverage_record='Default beverage', addition_record='Default addition'):
    with open(file_name, "a") as f:
        f.write(beverage_record + "\n")
        f.write(addition_record + '\n')


def ask_user(choice_msg):
    while True:
        try:
            choice = int(input(choice_msg))
        except ValueError as e:
            print('{} ---> Input number 1 or 2'.format(e))
            continue
        if 0 < choice < 3:
            break
        else:
            print('That is not 1 or 2... Try again!')
    print('Your choice is {}\n'.format(choice))
    my_dict = {1: "yes", 2: "no"}
    return my_dict[choice]




