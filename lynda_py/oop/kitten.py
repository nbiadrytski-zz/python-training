from lynda_py.oop.Animal import Animal


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, victim):
        print(f'{self.name()} will kill all {victim}!')
