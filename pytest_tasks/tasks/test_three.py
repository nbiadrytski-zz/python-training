import pytest
from collections import namedtuple
"""Test the Task Data Type"""


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no params should invoke defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_these_please
def test_member_access():
    """Check .field functionality of nametuple"""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)


def test_list_contains():
    my_list = [1, 2, 3]
    assert 1 in my_list
    assert 4 not in my_list
    assert my_list[0] < my_list[1]
