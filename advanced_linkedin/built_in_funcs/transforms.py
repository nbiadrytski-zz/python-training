def filter_func(x):
    if x % 2 == 0:
        return False
    return True


def filter_func2(x):
    if x.isupper():
        return False
    return True


def square_func(x):
    return x**2


def to_grade(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 65 <= x < 70:
        return "D"
    return "F"


def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # filter creates an iterator that filters out values from a given sequence
    # pass a func to filter to perform a boolean test
    odds = list(filter(filter_func, nums))
    print(odds)

    lowers = list(filter(filter_func2, chars))
    print(lowers)

    # map creates an iterator that takes one or more sequences of values
    # and produces a new sequence by applying a given func to each value in the original sequences
    squares = list(map(square_func, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(to_grade, grades))
    print(letters)


if __name__ == "__main__":
    main()
