class Super:
    def hello(self):
        self.data1 = 'spam'


class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'


X = Sub()
print(X.__dict__)  # {}: instance namespace dict

print(X.__class__)  # <class '__main__.Sub'>: class of instance X

print(Sub.__bases__)  # (<class '__main__.Super'>,): superclass of class
print(Super.__bases__)  # (<class 'object'>,)


X.hola()
print(X.__dict__)  # {'data2': 'eggs'}
X.hello()
print(X.__dict__)  # {'data2': 'eggs', 'data1': 'spam'}

Y = Sub()
print(Y.__dict__)  # {}: each instance has an independent namespace dictionary
Y.test = 9
print(Y.__dict__)  # {'test': 9}
