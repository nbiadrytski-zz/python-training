a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# find common keys
print(a.keys() & b.keys())  # {'y', 'x'}

# Find keys in a that are not in b
print(a.keys() - b.keys())  # { 'z' }

# Find (key,value) pairs in common
print(a.items() & b.items())  # {('y', 2)}

# make a new dict with x and z keys removed
c = {key: a[key] for key in a.keys() - {'x', 'z'}}
print(c)  # {'y': 2}
