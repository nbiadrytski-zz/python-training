class Bar:
    _x = 5

    @classmethod  # often used when we need alternative constructor
    def get_power(cls):
        return cls._x ** 2

    @staticmethod  # to unite some logic in other methods
    def get_sum_static():
        return 3 + 3


b = Bar()
print(b.get_power())  # 25
print(Bar.get_power())  # 25

print(Bar.get_sum_static())  # 6
