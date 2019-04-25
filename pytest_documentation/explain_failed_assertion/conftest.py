from pytest_documentation.explain_failed_assertion.test_foocompare import Foo


def pytest_assertrepr_compare(op, left, right):
    """Can be used to explain failed assertions when comparing custom objects"""
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return [f'Comparing Foo instances --> vals: {left.val} != {right.val}']