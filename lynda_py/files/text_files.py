def main():
    infile = open('lines.txt', 'rt')  # read and text mode
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        # print(line.rstrip(), file=outfile)
        outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close()
    infile.close()
    print('\ndone.')


if __name__ == '__main__':
    main()
