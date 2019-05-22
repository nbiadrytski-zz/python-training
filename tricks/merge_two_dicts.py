x = {'a': 1, 'b': 6}
y = {'b': 3, 'c': 4}

z = {**x, **y}  # takes b key fro y

print(z)
# {'a': 1, 'b': 3, 'c': 4}
