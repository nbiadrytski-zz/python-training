from random import randint


class Cheese:
    def __init__(self, holes):
        self.holes = holes

    @classmethod
    def random_holes(cls):
        return cls(randint(0, 100))

    def __str__(self):
        return f'{self.holes}'


solid_cheese = Cheese(2)
print(solid_cheese)  # 0

holey_cheese = Cheese.random_holes()
print(holey_cheese)  # 95
