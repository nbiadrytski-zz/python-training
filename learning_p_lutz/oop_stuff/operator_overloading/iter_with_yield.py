class Squares:
    """Any function (method) that contains a yield statement is turned into a generator function.
       When called, it returns a new generator object with automatic retention of local scope and code position,
       an automatically created __iter__ method that simply returns itself, and an automatically created __next__ method
       that starts the function or resumes it where it last left off.
    """

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


a = Squares(1, 5)

for i in a:
    print(i)

for i in a:
    print(i, end=' ')

# 1
# 4
# 9
# 16
# 25
# 1 4 9 16 25