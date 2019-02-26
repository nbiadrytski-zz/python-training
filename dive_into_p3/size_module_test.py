from dive_into_p3 import bytes_to_human

print(bytes_to_human.approximate_size(4096, True))
print(bytes_to_human.approximate_size.__doc__)  # func attribute
print(bytes_to_human.approximate_size.__name__)
print(bytes_to_human.approximate_size.__init__())

# everything is an object in
# the sense that it can be assigned to a variable or passed as an argument to a function


def tuple_as_return(a, b):
    sum = a + b
    minus = a - b
    return sum, minus


print(tuple_as_return(4, 2))
