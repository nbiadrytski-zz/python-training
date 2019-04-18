import pytest
import tasks
from tasks import Task


# 1 =================================================
def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'BRIAN', True)
    initial_task_id = tasks.add(task)
    task_from_db = tasks.get(initial_task_id)
    # everything but the id should be the same
    assert equivalent(task_from_db, task)
# =================================================


def equivalent(t1, t2):  # t1 is Task object after id was added in db, t2 is initial Task object
    """Check two tasks for equivalence."""
    # Compare everything but the id field
    return (t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done)


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


# 2 =================================================
@pytest.mark.parametrize('task',  # task is Task object variable, can be a string with a comma-separated list of names
                         [Task('sleep', done=True),  # list of Task objects
                          Task('wake', 'brian'),
                          Task('breathe', 'BRIAN', True),
                          Task('exercise', 'BrIaN', False)])
def test_add_2(task):  # test will be run once for each task and report each as a separate test
    """Parametrize with one parameter."""
    initial_task_id = tasks.add(task)
    task_from_db = tasks.get(initial_task_id)
    assert equivalent(task_from_db, task)
# =================================================


# 3 ================================================= test identifier uses the
# parameter values in the report to make it readable
@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('eat eggs', 'BrIaN', False),
                          ])
def test_add_3(summary, owner, done):
    """Parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    initial_task_id = tasks.add(task)
    task_from_db = tasks.get(initial_task_id)
    assert equivalent(task_from_db, task)
# test_add_variety.py::test_add_3[sleep-None-False] PASSED
# test_add_variety.py::test_add_3[wake-brian-False] PASSED
# test_add_variety.py::test_add_3[breathe-BRIAN-True] PASSED
# test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED
# =================================================


# ================================================= task list is a variable
tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

tasks_ids = [f'Task({t.summary}, {t.owner}, {t.done})' for t in tasks_to_try]
# =================================================


# 4 =================================================
@pytest.mark.parametrize('task', tasks_to_try)  # list tasks_to_try is argvalues param
def test_add_4(task):
    initial_task_id = tasks.add(task)
    task_from_db = tasks.get(initial_task_id)
    assert equivalent(task_from_db, task)
# test_add_variety.py::test_add_4[task0] PASSED
#  test_add_variety.py::test_add_4[task1] PASSED
#  test_add_variety.py::test_add_4[task2] PASSED
#  test_add_variety.py::test_add_4[task3] PASSED
#  test_add_variety.py::test_add_4[task4] PASSED
# ================================================= But the readability of the output is hard to interpret


# 5 =================================================
# ids=tasks_ids is an optional parametrize() param
# which allows to make our own identifiers for each task data set: e.g. Task(sleep,None,True) is an id
# The ids parameter needs to be a list of strings the same length as the number of data sets.
@pytest.mark.parametrize('task', tasks_to_try, ids=tasks_ids)
def test_add_5(task):
    initial_task_id = tasks.add(task)
    task_from_db = tasks.get(initial_task_id)
    assert equivalent(task_from_db, task)
# test_add_variety.py::test_add_5[Task(sleep,None,True)] PASSED
# test_add_variety.py::test_add_5[Task(wake,brian,False)0] PASSED
# test_add_variety.py::test_add_5[Task(wake,brian,False)1] PASSED
# test_add_variety.py::test_add_5[Task(breathe,BRIAN,True)] PASSED
# test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)] PASSED

# To rerun one data set:
# $ pytest -v "test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)]"
# =================================================


# 6 =================================================
# You can also identify parameters by including an id right alongside the parameter value
# This is useful when the id cannot be derived from the parameter value.
@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    initial_task_id = tasks.add(task)
    task_from_db = tasks.get(initial_task_id)
    assert equivalent(task_from_db, task)
# tasks_proj/tests/func/test_add_variety.py::test_add_6[just summary]
# tasks_proj/tests/func/test_add_variety.py::test_add_6[summary/owner]
# tasks_proj/tests/func/test_add_variety.py::test_add_6[summary/owner/done]
# =================================================


# =================================================
@pytest.mark.parametrize('task', tasks_to_try, ids=tasks_ids)
class TestAdd:
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        initial_task_id = tasks.add(task)
        task_from_db = tasks.get(initial_task_id)
        assert equivalent(task_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data for multiple tests."""
        initial_task_id = tasks.add(task)
        task_from_db = tasks.get(initial_task_id)
        assert task_from_db.id == initial_task_id
# =================================================
