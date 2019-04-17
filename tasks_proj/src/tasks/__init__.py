"""
src/tasks/__init__.py file tells Python that the directory is a package.
Acts as the main interface to the package when someone uses import tasks.
Contains code to import specific functions from api.py so that cli.py and our test files
can access package functionality like tasks.add() instead of having to do tasks.api.add().
"""

from .api import (
    Task,
    TasksException,
    add,
    get,
    list_tasks,
    count,
    update,
    delete,
    delete_all,
    unique_id,
    start_tasks_db,
    stop_tasks_db
)

__version__ = '0.1.0'
