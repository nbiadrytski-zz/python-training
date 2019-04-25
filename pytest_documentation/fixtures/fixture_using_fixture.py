import pytest


class App:
    def __init__(self, smtp_connection):
        self.smtp_connection = smtp_connection


@pytest.fixture(scope="module")
def app(smtp_connection):  # # smtp_connection used from conftest.py
    return App(smtp_connection)


def test_smtp_connection_exists(app):
    assert app.smtp_connection