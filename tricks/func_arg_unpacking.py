def unpack_args(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}


unpack_args(*tuple_vec)  # 1 0 1
unpack_args(**dict_vec)  # 1 0 1
