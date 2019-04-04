class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class tree and all
    its objects' attrs at and above self
    """
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + f'{attr}\n'
            else:
                result += spaces + f'{attr}={getattr(obj, attr)}\n'
        return result

    def __listclass(self, a_class, indent):
        dots = '.' * indent
        if a_class in self.__visited:
            return f'\n{dots}<Class {a_class.__name__}, address {id(a_class)}: (see above)>\n'
        else:
            self.__visited[a_class] = True
            here = self.__attrnames(a_class, indent)
            above = ''
            for super in a_class.__bases__:
                above += self.__listclass(super, indent+4)
            return f'\n{dots}<Class {a_class.__name__}, address {id(a_class)}:\n{here}{above}{dots}>\n'

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{here}{above}>'



