import pytest
from collections import namedtuple
"""Test the Task Data Type"""


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Task('do something', 'Nick', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'Nick',
                'done': True,
                'id': 21}
    assert t_dict == expected


@pytest.mark.run_these_please
def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected