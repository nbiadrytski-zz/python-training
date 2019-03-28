class SuperClass:
    def method(self):
        print('in SuperClass.method()')


class SubClass(SuperClass):
    def method(self):
        print('starting SubClass.method()')
        SuperClass.method(self)
        print('ending SubClass.method()')


x = SubClass()
x.method()
# starting SubClass.method()
# in SuperClass.method()
# ending SubClass.method()
