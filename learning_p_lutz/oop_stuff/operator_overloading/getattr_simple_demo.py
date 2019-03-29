class Empty:

    def __getattr__(self, attr_name):
        if attr_name == 'age':
            return 32
        else:
            raise AttributeError(f'attr "{attr_name}" does not exist')

    def __setattr__(self, attr_name, value):
        if attr_name == 'gender':
            self.__dict__[attr_name] = value + ': are you sure?'
        else:
            raise AttributeError(f'attr "{attr_name}" is not allowed')


X = Empty()

print(X.age)  # 32: dynamically computed attribute
# print(X.name)  # AttributeError: "name" attr does not exist

X.gender = 'male'
print(X.gender)  # male: are you sure?
# X.gg = 'test'  # AttributeError: attr "gg" is not allowed
