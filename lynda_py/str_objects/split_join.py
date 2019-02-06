s = 'This is a long string with a bunch of words in it.'

print(s.split())  # ['This', 'is', 'a', 'long', 'string', 'with', 'a', 'bunch', 'of', 'words', 'in', 'it.'] -> list

print(s.split('i'))  # ['Th', 's ', 's a long str', 'ng w', 'th a bunch of words ', 'n ', 't.']

l = s.split()
s2 = ':'.join(l)
print(s2)  # This:is:a:long:string:with:a:bunch:of:words:in:it.


