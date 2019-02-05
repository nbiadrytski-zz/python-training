animals = ('bear', 'bunny', 'dog', 'cat', 'pig')

for pet in animals:
    if pet == 'dog':
        continue
    #if pet == 'cat':
    #    break
    print(pet)
else:
    print('That is all of the animals')