class ListInherited:
    """
    Use dir() to collect both instance attrs and names inherited from its classes
    """
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':  # if attr starts with __ and ends with __
                result += f'\t{attr}\n'  # add attr without value
            else:
                result += f'\t{attr}={getattr(self, attr)}\n'
        return result

    # def __attrnames(self, indent=' '*4):
    #     result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-' * 77, indent, '-' * 77)
    #     unders = []
    #     for attr in dir(self):
    #         if attr[:2] == '__' and attr[-2:] == '__':
    #             unders.append(attr)
    #         else:
    #             display = str(getattr(self, attr))[:82 - (len(indent) + len(attr))]
    #             result += '%s%s=%s\n' % (indent, attr, display)
    #     return result % ', '.join(unders)

    def __str__(self):  # class name, address, attributes name=value
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attrnames()}>'
