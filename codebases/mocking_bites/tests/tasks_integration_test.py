from lib.task_list import *
from lib.task import *
from lib.task_formatter import *


def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]


def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True

def test_returns_list_of_all_tasks():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.all() == [task_1, task_2]

def test_marks_one_task_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    assert task_list.all_complete() == False

"""
Tests that incomplete task returns [ ]
"""
def test_incomplete_task_returns_not_complete_format():
    task = Task("My task")
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "[ ] My task"

"""
Tests that complete task returns [x]
"""
def test_complete_task_returns_complete_format():
    task = Task("My task")
    task_formatter = TaskFormatter(task)
    task.mark_complete()
    assert task_formatter.format() == "[x] My task"
