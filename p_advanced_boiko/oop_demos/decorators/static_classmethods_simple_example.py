class StaticClassMethods:

    @staticmethod
    def static_method():
        print('this is static method')

    @classmethod
    def class_method(cls):
        print(f'{type(cls)}, this is class method')


decorators = StaticClassMethods()

decorators.static_method()  # this is static method
StaticClassMethods.static_method()  # this is static method

decorators.class_method()  # <class 'type'>, this is class method
StaticClassMethods.class_method()  # <class 'type'>, this is class method
