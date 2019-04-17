import pytest
import tasks


def test_add_raises():
    """
    add() should raise an exception with wrong type param.
    If no exception is raised, the test fails.
    If the test raises a different exception, it fails.
    """
    with pytest.raises(TypeError):  # whatever is in the next block of code should raise a TypeError exception
        tasks.add(task='not a task Object')


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:  # excinfo is of type ExceptionInfo
        tasks.start_tasks_db('some/cool/path', 'mysql')
    exception_msg = excinfo.value.args[0]  # the first (and only) parameter to the exception matches a string
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
