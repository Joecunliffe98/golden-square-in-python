from lib.to_do_list import *
from lib.to_do import *

"""
Given a task
#adds it to the todo list
"""
def test_task_adds_to_todo_list():
    task_1 = Todo("Task 1")
    todo_list = TodoList()
    todo_list.add(task_1)
    assert todo_list.list_of_todo == [task_1]

"""
Given two tasks
#adds them to the todo list
"""
def test_multiple_task_adds_to_todo_list():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.list_of_todo == [task_1, task_2]

"""
Given one complete task and one incomplete task
#returns a list of the incomplete tasks
"""
def test_incomplete_list():
    task_1 = Todo("Task 1")
    task_1.mark_complete()
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_2]

"""
Given one complete task and one incomplete task
#returns a list of the completed tasks
"""
def test_complete_list():
    task_1 = Todo("Task 1")
    task_1.mark_complete()
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.complete() == [task_1]

"""
Given two incomplete tasks
#marks all tasks as complete and returns complete list
"""
def test_give_up():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    assert todo_list.complete() == [task_1, task_2]

