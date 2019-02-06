def main():
    x = dict(Buffy='meow', Zilla='grr', Tommy='murrr')
    kitten(**x)


def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow!!!')


if __name__ == '__main__':
    main()