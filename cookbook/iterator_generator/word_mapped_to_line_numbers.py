from collections import defaultdict
import pprint as pp

"""Map words in a file to the lines in which they occur"""

word_summary = defaultdict(list)

with open('oop_principles.txt') as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    # make each line is as a list of words ['-', 'the', 'functionality', 'is', 'defined', 'in', 'one']
    words = [w.strip().lower() for w in line.split()]  # strip removes spaces
    for word in words:
        word_summary[word].append(index)

pp.pprint(word_summary)  # e.g. {'data': [0, 3, 4],}
# The value for each word-key will
# be a list of line numbers that word occurred on. If the word occurred twice on a single
# line, that line number will be listed twice,
