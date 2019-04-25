import pytest


@pytest.fixture  # the result of a fixture is needed multiple times in a single test.
def make_customer_record():
    def _make_customer_record(name):
        return {'name': name, 'orders': []}
    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    print(customer_1)
    customer_2 = make_customer_record("Mike")
    print(customer_2)
    customer_3 = make_customer_record("Meredith")
    print(customer_3)