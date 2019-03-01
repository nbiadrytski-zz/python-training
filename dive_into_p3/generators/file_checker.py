def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line


def grep(pattern, lines):
    return (line for line in lines if pattern in line)


def printlines(lines):
    for line in lines:
        print(line)


def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)


main('of list', ['a_1.txt', 'b_1.txt'])