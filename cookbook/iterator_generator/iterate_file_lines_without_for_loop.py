"""
You need to process items in an iterable, but for whatever reason, you can’t or don’t want to use a for loop.
"""

with open('a_1.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')