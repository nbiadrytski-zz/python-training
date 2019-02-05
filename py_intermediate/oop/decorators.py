def add_wrapping(item):
    def wrapped_item():
        return 'A wrapped up box of {}'.format(str(item))
    return wrapped_item


@add_wrapping
def new_gpu():
    return 'A new Tesla P100 GPU'


# @add_wrapping
# def new_bicycle():
#     return 'a new bike'


print(new_gpu())
#print(new_bicycle())
