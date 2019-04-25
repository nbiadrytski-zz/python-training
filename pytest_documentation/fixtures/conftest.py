import pytest
import smtplib


@pytest.fixture(scope='module')
def smtp_connection():
    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
    yield connection # provide the fixture value
    print('\nteardown smtp')
    connection.close()

