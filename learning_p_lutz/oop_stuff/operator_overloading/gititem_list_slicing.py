class Slicer:

    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print(f'getitem: {index}')
        return self.data[index]


S = Slicer()

print(S[0])
# getitem: 0
# 5

print(S[:])  # Slicing sends __getitem__ a slice object
# getitem: slice(None, None, None)
# [5, 6, 7, 8, 9]
