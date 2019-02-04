# list comprehension stored in memory

list1 = [i for i in range(5)]
print(list1)

list2 = []
for i in range(5):
    list2.append(i)
print(list2)


# generator expressions will not be stored in memory
list3 = (i for i in range(5))  # use () instead of []
print(type(list3))
for i in list3:
    print(i)
