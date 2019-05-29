# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

h = ''

if x == 1 or y == 1 or x == 1:
    print('passed')  # passed

if 1 in (x, y, z):
    print('passed')  # passed

# These only test for true/false:
# if x or y or z is not 0
if x or y or z:  # as y = 1 'passed' will be printed, 0 means false
    print('passed')  # passed

if any((x, y, z)):  # if any is not 0
    print('passed')  # passed

if h:  # if string h is not empty
    print('passed')  # will not be printed
