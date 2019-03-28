class Super:
    """Defines a method function and a delegate that expects an action in a subclass"""
    def method(self):
        print('in Super.method()')  # default behavior

    def delegate(self):
        self.action()

    def action(self):
        raise NotImplementedError('action() must be defined!!!')


class Inheritor(Super):
    """Doesn’t provide any new names, so it gets everything defined in Super"""
    pass


class Replacer(Super):
    """Overrides Super’s method with a version of its own"""
    def method(self):
        print('in Replacer.method()')


class Extender(Super):
    """Customizes Super’s method by overriding and calling back to run the default"""
    def method(self):
        print('starting Extender.method()')
        Super.method(self)
        print('ending Extender.method()')


class Provider(Super):
    """Implements the action method expected by Super’s delegate method"""
    def action(self):
        print('in Provider.action()')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print(f'\n{klass.__name__}...')
        klass().method()

# Inheritor...
# in Super.method()
#
# Replacer...
# in Replacer.method()
#
# Extender...
# starting Extender.method()
# in Super.method()
# ending Extender.method()
    x = Provider()
    x.delegate()  # in Provider.action()
