def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print('Meow!!!')
    return 42


if __name__ == '__main__':
    main()