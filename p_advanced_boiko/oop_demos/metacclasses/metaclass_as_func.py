def func(class_name, superclasses, dict):
    dict['inner_string'] = dict.get("inner_string", "%s") % class_name
    return type('str', superclasses, dict)


class Cls(metaclass=func):
    inner_string = 'Hello %s'


a = Cls()
print(type(a))  # <class '__main__.Cls'>
print(a.inner_string)  # None