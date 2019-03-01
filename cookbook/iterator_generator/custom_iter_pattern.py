"""
If you want to implement a new kind of iteration pattern,
define it using a generator function.
Here’s a generator that produces a range of floating-point numbers
"""


#  generator function only runs in response to “next” operations carried out in iteration
def floats_range(start, stop, increment):
    x = start
    while x < stop:
        yield x  # presence of the yield statement in a function turns it into a generator
        x += increment


# iterate over floats_range using a for loop
for number in floats_range(3, 9, 0.5):
    print(number)

# use floats_range with some other function that consumes an iterable (e.g., sum(), list(), etc.)
result_list = list(floats_range(3, 9, 0.5))
print(result_list)  # [3, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5]
