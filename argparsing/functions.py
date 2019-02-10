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
    beverage_to_sell = input('Which beverage will you sell?: {}'.format(available_beverages))
    beverage_price = input('Enter price: ')
    sale_record = 'Beverage: {}. Price: {}$'.format(beverage_to_sell, str(beverage_price))
    return sale_record


def add_ingredient(available_additions):
    addition_to_sell = input('Which addition will you add?: {}'.format(available_additions))
    addition_price = input('Enter price: ')
    sale_record = 'Addition: {}. Price: {}$'.format(addition_to_sell, str(addition_price))
    return sale_record


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
    print('Your choice is {}'.format(choice))
    my_dict = {1: "yes", 2: "no"}
    return my_dict[choice]




