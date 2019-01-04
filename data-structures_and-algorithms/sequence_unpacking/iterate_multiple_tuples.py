records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4), ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *values in records:
    if tag == 'foo':
        do_foo(*values)
    elif tag == 'bar':
        do_bar(*values)


print("===============================================================================================")

# Star unpacking can also be useful when combined with certain kinds of string processing
# operations, such as splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)  # nobody
print(fields)  # ['*', '-2', '-2', 'Unprivileged User']
print(homedir)  # /var/empty
print(sh)  # /usr/bin/false

