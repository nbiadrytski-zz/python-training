x = 42
y = 73
z = 42 * 747 * 1000

print('the number is {} {}'.format(x, y))  # the number is 42 73

print('the number is {1} {0}'.format(x, y))  # the number is 73 42

print('the number is {1} {0} {1}'.format(x, y))  # the number is 73 42 73

# formatting instructions
print('the number is {0:<5} {1:>5} test'.format(x, y))  # the number is 42       73 test

print('the number is {:,}'.format(z))  # the number is 31,374,000

print('the number is {:,}'.format(z).replace(',', '.'))  # the number is 31.374.000

print('the number is {:.3f}'.format(z))  # the number is 31374000.000; 3 chars after dot

print(f'the number is {z}')  # the number is 31374000

