from lib.recipe_1 import *
import pytest

"""
Given a passage of text that returns exact minutes
Returns the time value in minutes
"""
def test_reading_time_calculator_exact_minutes():
    assert reading_time_calculator(200) == "1 minute to read"

"""
Given a passage that will not take exact minutes
Return the time value in minutes and seconds
"""
def test_reading_time_calculator_over_one_minute():
    assert reading_time_calculator(300) == "1 minute 30 seconds to read"

"""
Given a passage that will take less than 1 minute
Return a time value in seconds
"""
def test_reading_time_calculator_less_one_minute():
    assert reading_time_calculator(100) == "30 seconds to read"

"""
Given an empty passage
Return a message saying no text provided
"""
def test_reading_time_calculator_empty_passage():
    assert reading_time_calculator(0) == "No text provided"

"""
Given a passage that will take less than 1 second to read
Return message saying that you can read this in less than 1 second
"""
def test_reading_time_calculator_less_one_second():
    assert reading_time_calculator(1) == "Less than 1 second to read"

"""
Given a None value
An error is thrown
"""
def test_reading_time_calculator_error_thrown():
    with pytest.raises(Exception) as e:
        reading_time_calculator(None)
    error_message = str(e.value)
    assert error_message == "Error: None"
