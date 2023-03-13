from lib.task_formatter import *
from unittest.mock import Mock

"""
Tests that incomplete task returns [ ]
"""
def test_incomplete_task_returns_not_complete_format():
    task = Mock()
    task_formatter = TaskFormatter(task)
    task.title = "My task"
    task.complete = False
    assert task_formatter.format() == "[ ] My task"

"""
Tests that complete task returns [x]
"""
def test_complete_task_returns_complete_format():
    task = Mock()
    task_formatter = TaskFormatter(task)
    task.title = "My task"
    task.complete = True
    assert task_formatter.format() == "[x] My task"