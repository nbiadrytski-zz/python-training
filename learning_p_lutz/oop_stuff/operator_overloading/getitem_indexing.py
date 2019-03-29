class Indexer:

    def __getitem__(self, index):  # instance-indexing operations
        return index ** 2


X = Indexer()

for i in range(5):
    print(X[i], end=' ')  # 0 1 4 9 16
