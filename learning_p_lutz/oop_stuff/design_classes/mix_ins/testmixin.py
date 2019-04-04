import importlib


def tester(listerclass, sept=False):

    class Super:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)


def test_by_names(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)


if __name__ == '__main__':
    #test_by_names('listinstance', 'ListInstance', True)  # file listinstance.py and its Class ListInstance
    #test_by_names('listinherited', 'ListInherited', False)  # file listinherited.py and its Class ListInherited
    test_by_names('listtree', 'ListTree', False)  # file listinherited.py and its Class ListInherited

