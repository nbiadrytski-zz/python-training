from lynda_py.oop.Animal import Animal


class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)
