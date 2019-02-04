import timeit


# input_list = range(100)
#
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
#
# xyz_gen = (i for i in input_list if div_by_five(i))
#
# xyz_list = [i for i in input_list if div_by_five(i)]


# test how fast you code snippet is; run your code 5000 times
print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz_gen = (i for i in input_list if div_by_five(i))

xyz_list = [i for i in input_list if div_by_five(i)]''', number=5000))


