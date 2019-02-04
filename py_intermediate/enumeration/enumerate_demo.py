example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

print("="*32)

# another way
for i, j in enumerate(example):
    print(i, j)

print("="*32)

new_dict = dict(enumerate(example))
print(new_dict)  # {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
