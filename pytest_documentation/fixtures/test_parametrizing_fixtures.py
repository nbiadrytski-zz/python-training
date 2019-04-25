import pytest
import smtplib


@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"], ids=['gmail', 'python'])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection}")
    smtp_connection.close()


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250