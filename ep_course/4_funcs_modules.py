money = 2000


def add_money():
    global money
    money = money + 1  # now we use global var money defined before func
    print(money)


def my_sum(number: int):
    new_number = number + 1
    print(locals())  # print local vars


add_money()  # 2001
print(money)  # 2001

my_sum(1)  # {'new_number': 2, 'number': 1}


my_add = lambda a, b: a + b
print(my_add(2, 5))  # 7
