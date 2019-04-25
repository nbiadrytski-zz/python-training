import pytest


class DB:
    """
    We have a database fixture which has a begin/rollback/commit architecture
    and we want to automatically surround each test method by a transaction and a rollback
    """
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        self.intransaction.append(name)

    def rollback(self):
        self.intransaction.pop()


@pytest.fixture(scope="module")
def db():
    return DB()

# if you put the transact definition into a conftest.py file without using autouse
# content of conftest.py
# @pytest.fixture
# def transact(request, db):
#     db.begin()
#     yield
#     db.rollback()
# and then have a TestClass using it by declaring the need:
# @pytest.mark.usefixtures("transact")
class TestClass:
    """
    The class-level transact fixture is marked with autouse=true
    which implies that all test methods in the class will use this fixture
    without a need to state it in the test function signature or with a class-level usefixtures decorator
    """
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        assert db.intransaction == ["test_method2"]