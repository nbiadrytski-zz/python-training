class StepperIndex:

    def __getitem__(self, i):
        return self.data[i]


X = StepperIndex()
X.data = 'Spam'

for item in X:
    print(item, end=' ')  # S p a m

print('\n')

print([c for c in X])  # ['S', 'p', 'a', 'm']

print(list(map(str.upper, X)))  # ['S', 'P', 'A', 'M']
