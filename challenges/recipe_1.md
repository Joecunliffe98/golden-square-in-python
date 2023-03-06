## 1. Describe the Problem

User wants to be able to manage their time while reading

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def reading_time_calculator(passage):
    """Shows how much time it will take to read the provided passage

    Parameters: 
        passage: a string that contains all of the text that the user wants to read

    Returns: 
        A time value in minutes
        

    Side effects: 
        This function will print a time value in minutes
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a passage of text that returns exact minutes
Returns the time value in minutes
"""
reading_time_calculator(200 words) => [1 minute]

"""
Given a passage that will not take exact minutes
Return the time value in minutes and seconds
"""
reading_time_calculator(300 words) => [1 minute 30 seconds]

"""
Given a passage that will take less than 1 minute
Return a time value in seconds
"""
reading_time_calculator(100 words) => [30 seconds]

"""
Given an empty passage
Return a message saying no text provided
"""
reading_time_calculator("") => "No text provided"

"""
Given a passage that will take less than 1 second to read
Return message saying that you can read this in less than 1 second
"""
reading_time_calculator(1 word) => "You can read this in less than 1 second"

"""
Given a None value
An error is thrown
"""
reading_time_calculator(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!