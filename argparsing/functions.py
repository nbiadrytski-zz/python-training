import re


def save_sale_to_file(file_name, value):
    with open(file_name, "a") as f:
        f.write(value + '\n')


def read_sale_from_file(file_name):
    total_price = []
    try:
        with open(file_name, "r") as f:
            for line in f:
                result = re.findall(r'\d+', line)
                price = int(result[0])
                total_price.append(price)
                print(line)
        print('Total Price: ', sum(total_price))
    except TypeError as e:
        print('Invalid filename or no file passed... ', e)

