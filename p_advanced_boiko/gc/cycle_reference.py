import sys


class Class:
    def __del__(self):
        print('deleted!!!')
    pass


c1 = Class()
c2 = Class()

print(f'c1 ID: {id(c1)}, c2 ID: {id(c2)}')
print(f'c1 refs count: {sys.getrefcount(c1)}, c2 refs count: {sys.getrefcount(c2)}\n')

c1.ref = c2
c2.ref = c1
print(f'c1.ref ID: {id(c1.ref)}, c2.ref ID: {id(c2.ref)}')
print(f'c1 refs count: {sys.getrefcount(c1)}, c2 refs count: {sys.getrefcount(c2)}\n')

del c1.ref, c2.ref
print('Deleted c1.ref and c2.ref\n')

print(f'c1 refs count: {sys.getrefcount(c1)}, c2 refs count: {sys.getrefcount(c2)}\n')

del c1, c2

# print(f'c1 refs count: {sys.getrefcount(c1)}, c2 refs count: {sys.getrefcount(c2)}\n') --> will fail
# NameError: name 'c1' is not defined


