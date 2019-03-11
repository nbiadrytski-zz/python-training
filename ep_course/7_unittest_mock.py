from unittest.mock import MagicMock


class A:
    def method(self, a, b, c, key):
        return 666


thing = A()
thing.method = MagicMock(return_value=13)
print(thing.method(3, 4, 5, key='value'))  # will return 13

thing.method.assert_called_with(3, 4, 5, key='value')