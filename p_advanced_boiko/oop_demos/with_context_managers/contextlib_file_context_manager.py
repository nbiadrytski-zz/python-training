from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()


files = []

for x in range(5):
    with open_file('foo.txt', 'w') as my_file:
        files.append(my_file)

print(len(files))  # 5
