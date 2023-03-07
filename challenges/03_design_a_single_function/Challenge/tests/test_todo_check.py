import pytest
from lib.todo_check import *

def test_check_to_do_one_string():
    task_list = ["#TODO Take out rubbish", "Clean up room"]
    assert check_to_do(task_list) == ["#TODO Take out rubbish"]
    
def test_check_to_do_multiple_strings():
    task_list = ["#TODO Take out rubbish", "#TODO Clean up room", "Feed dog"]
    assert check_to_do(task_list) == ["#TODO Take out rubbish", "#TODO Clean up room"]

def test_check_to_do_no_tasks():
    task_list = [["Take out rubbish", "Clean up room", "Feed dog"]]
    assert check_to_do(task_list) == "Nothing in to do list"

def test_check_to_do_input_empty():
    task_list = []
    assert check_to_do(task_list) == "Input list is empty"

def test_check_to_do_error():
    with pytest.raises(Exception) as e:
        check_to_do(None)
    error_message = str(e.value)
    assert error_message == "Error: None value passed as argument"