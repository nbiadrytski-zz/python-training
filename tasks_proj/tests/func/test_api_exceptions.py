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


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


def test_delete_raises():
    """delete() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.delete(task_id=(1, 2, 3))


class TestUpdate:
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1}, task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')
