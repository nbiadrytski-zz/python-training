class Truth:

    def __bool__(self):  # tries __bool__ first
        return True

    def __len__(self, other):  # tries __len__ then
        return 0


X = Truth()

if X:
    print('yes!')  # yes!

print(bool(X))  # True
