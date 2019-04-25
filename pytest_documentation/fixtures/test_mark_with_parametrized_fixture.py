import pytest


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass

# ===================== 2 passed, 1 skipped in 0.03 seconds ======================..s
