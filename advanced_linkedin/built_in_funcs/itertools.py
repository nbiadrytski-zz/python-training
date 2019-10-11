import itertools


def t_function(x):
    return x < 40

MESSAGE_NOT_MATCH_PATTERN = 'Known messages: {}'


def main():
    # cycle infinite iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use infinite count to create a simple counter
    count1 = itertools.count(start=100, step=10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,44,60, 11]
    # by default adds neighboring values
    acc = itertools.accumulate(vals)  # [10, 30, 60, 100, 150, 190, 220]
    print(list(acc))

    # apply max built in
    # one by one, if biggest number is found it is printed then
    acc = itertools.accumulate(vals, max)  # [10, 20, 30, 40, 50, 50, 50]
    print(list(acc))

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    # dropwhile will drop values from the sequence while t_function returns true
    print(list(itertools.dropwhile(t_function, vals)))  # ignore values until 40
    print(list(itertools.takewhile(t_function, vals)))  # return values until 40

def ret_chain():
    b =  itertools.chain("ABCD", "1234")
    raise Exception(MESSAGE_NOT_MATCH_PATTERN.format([m for m in b]))


if __name__ == "__main__":
    #main()
    v = ret_chain()
