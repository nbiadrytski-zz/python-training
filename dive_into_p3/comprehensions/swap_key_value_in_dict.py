a_dict = {'a': 1, 'b': 2, 'c': 3}

swapped_dict = {value: key for key, value in a_dict.items()}
print(swapped_dict)  # {1: 'a', 2: 'b', 3: 'c'}
