class MyNumbers:
    def __iter__(self):
        self.a = 9
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


obj = MyNumbers()
my_iterator = iter(obj)


for number in my_iterator:
    print(number)
