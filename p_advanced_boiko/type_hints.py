from decimal import Decimal
from typing import NewType


class Cheese:
    def __init__(self, name, price):
        self.name = name
        self.price = price


Price = NewType('Price', Decimal)


def cheeseshop(kind: Cheese, weight: float, region: str=None) -> Price:
    print(f'From {region}!!!')
    return weight * kind.price


mozarella = Cheese('Mozarella', 0.99)

print(cheeseshop(mozarella, 2.5, 'France'))