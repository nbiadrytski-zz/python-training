from collections import deque

'''performs a simple text match on a sequence of lines and yields the
matching line along with the previous N lines of context when found'''


# generator function
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('test.txt') as f:
        for line, prevlines in search(f, 'trust', 3):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)