from lynda_py.oop.Animal import Animal
from lynda_py.oop.kitten import Kitten
from lynda_py.oop.duck import Duck


def main():
    animal = Animal(type='dog', name='Jimmy', sound='murr')

    print((Animal(type='velociraptor', name='veronica', sound='hello')))

    print(Animal())  # printing Animal without attributes

    animal.sound('bark')  # using setter
    print(animal.sound())  # using getter
    print(animal)  # printing a1 object using __str__ method

    kitten = Kitten(name='Barsik', sound='meoow')
    duck = Duck(name='Donald', sound='Quack')
    print(kitten)
    print(duck)

    kitten.kill('mice')


if __name__ == '__main__':
    main()