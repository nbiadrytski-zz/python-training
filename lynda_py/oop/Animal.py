class Animal:
    x = [1, 2, 3]  # class var

    def __init__(self, **kwargs):
        # object vars
        # this is encapsulation - my vars belong to the object, not to the class
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    # setter and getter
    def type(self, type=None):
        if type:
            self._type = type
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, name=None):
        if name:
            self._name = name
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, sound=None):
        if sound:
            self._sound = sound
        try:
            return self._sound
        except AttributeError:
            return None

    def __str__(self):  # object string representation
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'  # using getter

