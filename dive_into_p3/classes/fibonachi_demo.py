from dive_into_p3.classes.fibonachi import Fib

#for n in Fib(1000):
#    print(n, end=', ')

fib = Fib(1000)
fib.__iter__()  # returns iterator object
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
