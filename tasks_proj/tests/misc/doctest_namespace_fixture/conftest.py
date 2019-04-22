import pytest
from tasks_proj.tests.misc.doctest_namespace_fixture import unnecessary_math


@pytest.fixture(autouse=True)
def add_um(doctest_namespace):
    doctest_namespace['um'] = unnecessary_math