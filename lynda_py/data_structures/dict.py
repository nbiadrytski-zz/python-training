def main():
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
               'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    print_dict(animals)


def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
