class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via inheritance of __str__ coded here;
    !!! displays instance attrs only with the help of __dict__;
    self is instance of lowest class; __X names avoid clashing with client's attrs
    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):  # __dict__ holds instance attributes
            result += f'\t{attr}={self.__dict__[attr]}\n'
        return result

    def __str__(self):  # class name, address, attributes name=value
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attrnames()}>'
