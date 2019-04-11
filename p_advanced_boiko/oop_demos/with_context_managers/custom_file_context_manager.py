class MyFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        print('-------------entering------------------')
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
        print('-------------exiting-----------------')


files = []

for _ in range(5):
    with MyFile('foo.txt', 'w') as my_file:
        my_file.write('foo')
        files.append(my_file)
print(len(files))