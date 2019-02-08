import re


def is_manager(args):
    if args.position[0].lower() == 'manager':
        return True


def is_salesperson(args):
    if args.position[0].lower() == 'salesperson':
        return True


def save_sale_to_file(file_name, value):
    with open(file_name, "a") as f:
        f.write(value + '\n')


def salesperson_records(file):
    total_price = []
    for line in file:
        try:
            result = re.findall(r'\d+', line)
            price = int(result[0])
            total_price.append(price)
            print(line)
        except IndexError as e:
            print('Sale price is missing in {} line --> {}'.format(line, e))
    print('Total Price: ', sum(total_price))
