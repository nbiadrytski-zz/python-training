l = [1, 2, 3]
print(l + l)  # [1, 2, 3, 1, 2, 3]
print(l * 2)  # [1, 2, 3, 1, 2, 3]
print(l)  # [1, 2, 3]

a = l  # assign l to a
print(a)  # [1, 2, 3]
a[0] = 666  # change 0's elem of a
print(a)  # [666, 2, 3]
print(l)  # [666, 2, 3]; l 0's elem is changed as well

for number in a:
    print(f'My number: {number}')
# My number: 666
# My number: 2
# My number: 3

print(dir(a))  # object's attributes and methods
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
#  '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
#  'pop', 'remove', 'reverse', 'sort']

a.append(9)
print(a)  # [666, 2, 3, 9]

b = [1, 2, 3, 1, 6, 8, 1]
print(b.count(1))  # 3; digit 1 occurs 3 times in b

b.extend([99, 88])
print(b)  # [1, 2, 3, 1, 6, 8, 1, 99, 88]

t = (1, 2, 3)
print(t)  # (1, 2, 3); tuple

d = {1: 'qwerty', 2: 'test'}
print(d)  # {1: 'qwerty', 2: 'test'}

# create dict via dict func
d1 = dict(number=123, test='test')
print(d1)  # {'number': 123, 'test': 'test'}
print(d1['number'])  # 123
d1['number'] = 666
print(d1)  # {'number': 666, 'test': 'test'}

print(hash('test'))  # 447348076465211546
# print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'
# dict keys can be only hashable types

d2 = {1: 2, 3: 4, 5: 6}
print(list(d2.keys()))  # [1, 3, 5]
print(list(d2.values()))  # [2, 4, 6]
print(d.get(9))  # None; safe way to get key even if it doesn't exist
print(d.get(9, 'No such key'))  # No such key

for key, value in d2.items():
    print(f'Key - {key}, Value - {value}')
# Key - 1, Value - 2
# Key - 3, Value - 4
# Key - 5, Value - 6

d3 = {}
if d3:
    print('Hi')  # nothing will be printed

if d3 is not None:
    print('Hi')  # Hi will be printed





