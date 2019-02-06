import sys


def main():
    try:
        x = 7/0
    except ValueError:
        print('I caught a value error')
    except:
        print(f'Unknown error: {sys.exc_info()[1]}')
    else:
        print('Good job')
        print(x)


if __name__ == '__main__':
    main()
