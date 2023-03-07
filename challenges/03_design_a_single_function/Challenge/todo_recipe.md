## 1. Describe the Problem

> As a user  
> So that I can keep track of my tasks  
> I want to check if a text includes the string `#TODO`.

## 2. Design the Function Signature

```python

def check_to_do(list_of_tasks):
    """
    Check if each string in list contains the phrase "#TODO'. If it does then add to new list. Return new list.


    Parameters: 
        
        list_of_tasks: List (contain multiple strings representing tasks that the user has)

    Returns: 
        
        Returns a new list as a list variable with only the tasks that contain to do phrase

    Side effects: 
        No side effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests


```python

"""
Checks if one #TODO string is returned in new list
"""
check_to_do(["#TODO Take out rubbish", "Clean up room"]) => ["#TODO Take out rubbish"]

"""
Checks if multiple #TODO strongs as returned in new list
"""
check_to_do(["#TODO Take out rubbish", "#TODO Clean up room", "Feed dog"]) => [["#TODO Take out rubbish", "#TODO Clean up room"]]

"""
Check if no #TODO in list return sentence saying nothing in to do list
"""
check_to_do(["Take out rubbish", "Clean up room", "Feed dog"]) => ["Nothing in to do list"]

"""
Check if input list is empty and return sentence saying input list is empty
"""
check_to_do([]) => ["Input list is empty"]

"""
Given a None value
An error is thrown
"""
check_to_do(None) => ["Error: None value passed as arguement]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

Ensure all test function names are unique, otherwise pytest will ignore them!