from lib.exercise import *
import pytest

def test_adds_task_to_list():
    new_task = Tasks()
    new_task.add_task("Walk the dog")
    assert new_task.see_tasks() == ["Walk the dog"]

def test_given_no_task_raise_exception():
    new_task = Tasks()
    with pytest.raises(Exception) as e:
        new_task.add_task("")
    error_message = str(e.value)
    assert error_message == "No task set."

def test_complete_task_removes_from_list():
    new_task = Tasks()
    new_task.add_task("Walk the dog")
    assert new_task.see_tasks() == ["Walk the dog"]
    new_task.complete_task("Walk the dog")
    assert new_task.see_tasks() == []
