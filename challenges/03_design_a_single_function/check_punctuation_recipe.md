# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar

I want to verify that a text starts with a capital letter and ends 
with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

Function Name: Check_Punctuation() 

Parameters: One String, of any length. 

Returns: 

Variation one: a Boolean - If the string starts with a capital letter and ends with a suitable sentence end character, the function simply returns True

Variation two: A String - A string explaining which of the two was missing. 

```python
# EXAMPLE

def check_punctuation()
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given anything other than a String - Returns Error Message
"""
check_punctuation(7) => ["Invalid Input - Not a String"]
 
"""
Given a string that starts with a Capital and Ends with . or ! or ?
returns True
"""
check_punctuation("Hello!") => [True]

"""
Given a string that starts with a Capital but doesn't end with a suitable character - returns a message:
"""
check_punctuation("Hello") => ["You didn't close the sentence!"]

"""
Given a string that starts with no Capital but does end with a suitable character - returns a message:
"""
check_punctuation("Hello") => ["You forgot your capital letter!"]

"""
Given a string that starts with no Capital and ends with no suitable character. Return a message: 
"""

check_punctuation("hello") => ["You forgot your capital letter, and your sentence does not close!"]

"""
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


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
