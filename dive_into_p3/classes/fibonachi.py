class Fib:
    """iterator that yields numbers in the Fibonacci sequence"""

    def __init__(self, max):
        self.max = max  # instance var

    # returns any object that implements a __next__() method.
    def __iter__(self):  # An iterator is just a class that defines an __iter__() method
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
