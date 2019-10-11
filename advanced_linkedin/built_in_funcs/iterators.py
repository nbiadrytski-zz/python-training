# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_fr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    # i is an iterable object created from days sequence
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue
    print(next(i))  # Wed
    print(next(i))  # Thu
    print(next(i))  # Fri
    print(next(i))  # Sat
    # print(next(i))  --> will not work: StopIteration

    # same as above, iterate over all days
    for i in iter(days):
        print(i)

    # iterate using a function and a sentinel
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # use regular iteration over the days
    for m in range(len(days)):
        print(m + 1, days[m])

    # using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # use zip to combine sequences
    for m in zip(days, days_fr):
        print(m)

    for i, m in enumerate(zip(days, days_fr), start=1):
        print(i, m[0], "=", m[1], "in French")


if __name__ == "__main__":
    main()
