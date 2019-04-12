from p_advanced_boiko.oop_demos.abstract_base_classes.abc_demo1_abstraction import Base


class Implementation(Base):  # need to implement load and save, otherwise error

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

# Base below is kind of a 'virtual parent' class of Implementation
# Base.register(Implementation)  # same as class Implementation(Base):


if __name__ == '__main__':
    # Is <class '__main__.Implementation'> a subclass of Base? True
    print(f'Is {Implementation} a subclass of Base? {issubclass(Implementation, Base)}')

    inst = Implementation()
    # Is <__main__.Implementation object at 0x10a9ddc50> an instance of Base? True
    print(f'Is {inst} an instance of Base? {isinstance(inst, Base)}')
