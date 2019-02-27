import re
import itertools

s = '100 NORTH BROAD ROAD'
# search the string s for the regular expression 'ROAD$' and replace it with 'RD.'
print(re.sub('ROAD$', 'RD.', s))  # matches 'ROAD' only when it occurs at the end of a string; ^ is the start of string

s1 = '100 BROAD ROAD APT. 3'
# match 'ROAD' when it’s a whole word by itself anywhere in the string
print(re.sub(r'\bROAD\b', 'RD.', s1))  # \b means a word boundary must occur right here

print(re.findall('[0-9]+', '16 2-by-4s in rows of 8'))  # find all digits ['16', '2', '4', '8']

print(re.findall('[A-Z]+', 'SEND + MORE == MONEY'))  # find all letters ['SEND', 'MORE', 'MONEY']


unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
# ord() method returns an integer representing Unicode code point for the given Unicode character
gen = (ord(c) for c in unique_characters) # generator expression
for a in gen:
    print(a)

# find 3 possible pairs from list
perms = itertools.permutations('ABC', 3)
for x in perms:
    print(x)

print(list(itertools.combinations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
