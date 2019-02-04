import os


names = ['Jeff', 'Garry', 'Jil', 'Samantha']

for name in names:
    print("Hi, " + name)
    # print(' '.join(['Hello,', name]))  # another way

print("#"*32)

# print the whole list as string
names_as_str = ', '.join(names)
print(type(names_as_str))  # <class 'str'>
print(names_as_str)  # Jeff, Garry, Jil, Samantha
print("#"*32)

location_of_file = '/Users/mikalai_biadrytski/Desktop'
file_name = 'example.txt'

with open(os.path.join(location_of_file, file_name)) as f:
    print(f.read())


