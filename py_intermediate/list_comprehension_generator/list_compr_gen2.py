input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))  # generator (doesn't create a list)
print(xyz)  # <generator object <genexpr> at 0x10fecc7d8>

xyz = [i for i in input_list if div_by_five(i)]  # list created, takes more memory
print(xyz)  # [5, 10, 15, 20, 5]
[print(i) for i in xyz]  # iterate over xyz list

print("="*32)

[[print(i, j) for j in range(5)] for i in range(5)]
print("="*32)
# same as
for i in range(5):
    for j in range(5):
        print(i, j)
print("="*32)

list_of_typles = [[(i, j) for j in range(5)] for i in range(5)]
print(type(list_of_typles))
print(list_of_typles)
print("="*32)

# embed into generator
xyz_generator = (((i, j) for j in range(5)) for i in range(5))
print(type(xyz_generator))

for i in xyz_generator:
    for j in i:
        print(j)
