from lib.to_do import *

"""
Given a task
#adds it as a task and makes sure it is not complete yet
"""
def test_add_task_and_check_not_complete():
    task_1 = Todo("Walk the dog")
    assert task_1.complete == False

"""
Given a task
#adds it as a task and sets it to complete
"""
def test_add_task_and_set_to_complete():
    task_1 = Todo("Walk the dog")
    task_1.mark_complete()
    assert task_1.complete == True