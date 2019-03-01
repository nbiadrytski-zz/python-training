import itertools


with open('b_1.txt') as f:
    for line in itertools.dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')