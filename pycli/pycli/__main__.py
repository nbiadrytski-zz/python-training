import sys
from .classmodule import MyClass
from .funcmodule import my_function


def main():
    print('in main')

    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_object = MyClass('Jimmy')
    my_object.say_name()

    my_function('Hello, World!')


if __name__ == '__main__':
    main()
