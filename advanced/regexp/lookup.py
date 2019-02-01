import optparse
import re


def main():
    parser = optparse.OptionParser("usage %prog -w <word> -f <file>")
    parser.add_option("-w", dest="word", type="string", help="specify a word to search")
    parser.add_option("-f", dest="fname", type="string", help="specify a file to search")

    (options, args) = parser.parse_args()

    if (options.word is None) | (options.fname is None):
        print(parser.usage)
        exit(0)
    else:
        word = options.word
        fname = options.fname

    search_file = open(fname)
    line_num = 0

    for line in search_file.readlines():
        line = line.strip("\n\r")
        line_num += 1
        search_result = re.search(word, line, re.M | re.I)
        if search_result:
            print(str(line_num) + ": " + line)

    search_file.close()


if __name__ == "__main__":
    main()

'''
$ python3 lookup.py -w main -f reg_exp.py
4: def main():
20: if __name__ == "__main__":
21:     main()
'''
