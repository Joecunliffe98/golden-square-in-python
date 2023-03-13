from unittest.mock import Mock
from lib.diary import *

"""
Tests that contents has been added to Diary
"""
def test_contents_added_to_diary():
    diary = Diary("My contents")
    assert diary.read() == "My contents"

"""
Tests that no contents returns empty string
"""
def test_no_contents_returns_empty_string():
    diary = Diary("")
    assert diary.read() == ""
