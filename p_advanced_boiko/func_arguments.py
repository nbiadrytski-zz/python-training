def hello(name, ending):  # required args
    print('Hello', name, ending)


def hello2(name, ending='!'):  # default arg
    print('Hello', name, ending)


def change_list(a, L=[]):  # don't add mutable objects(lists, dicts, etc. as default args
    L.append(a)
    return L


i = 5
def f(arg=i):
    print(arg)
i = 6


def join_items(separator, *items):  # arbitrary arguments list
    return separator.join(str(i) for i in items)


def printargs(arg, **kwargs):  # keyword arguments
    print(arg)
    print(kwargs)


def test_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


hello('Python', '!')  # Hello Python !: required args passed
hello('Python', ending='!')  # Hello Python !: positional arg, then keyword arg
#  hello(ending='!', 'Python') will fail, pos arg after keyword arg

hello2('Python', '!')  # Hello Python !
hello2('Python')  # Hello Python !
hello2('Python', '?')  # Hello Python ?

print(change_list(1))  # [1]
print(change_list(2))  # [1, 2]

f()  # 5

print(join_items('-', 1, 2, 3))  # 1-2-3
args = [3, 6]
print(join_items('-', *args))  # 3-6

printargs('pos argument', name1=1, name2=2)
# pos argument
# {'name1': 1, 'name2': 2}
my_dict = {"arg3": 3, "arg2": "two"}
printargs('pos arg', **my_dict)
# pos arg
# {'arg3': 3, 'arg2': 'two'}

test_var_args_call(1, **my_dict)
# arg1: 1
# arg2: two
# arg3: 3