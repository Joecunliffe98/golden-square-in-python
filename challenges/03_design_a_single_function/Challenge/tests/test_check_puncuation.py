from lib.check_punctuation import *
import pytest

"""
Given anything other than a String - Returns Error Message
"""
#check_punctuation(7) => ["Invalid Input - Not a String"]

def test_returns_error():
    with pytest.raises(Exception) as e:
        check_punctuation(5)
    message = str(e.value)
    assert message == "Invalid Input - Not a String"

"""
Given a string that starts with a Capital and Ends with . or ! or ?
returns True
"""
#check_punctuation("Hello!") => [True]

def test_behaves_correctly_with_suitable_input():
    result = check_punctuation("Hello, There!")
    assert result == True

"""
Given a string that starts with a Capital but doesn't end with a suitable character - returns a message:
"""
#check_punctuation("Hello") => ["You didn't close the sentence!"]

def test_ends_wrong():
    result = check_punctuation("Hello")
    assert result == "You didn't close the sentence!"
"""
Given a string that starts with no Capital but does end with a suitable character - returns a message:
"""
#check_punctuation("Hello") => ["You forgot your capital letter!"]

def test_no_capital():
    result = check_punctuation("hello!")
    assert result == "You forgot your capital letter!"

"""
Given a string that starts with no Capital and ends with no suitable character. Return a message: 
"""
#check_punctuation("hello") => ["You forgot your capital letter, and your sentence does not close!"]

def test_all_wrong():
    result = check_punctuation("hello")
    assert result == "You forgot your capital letter, and your sentence does not close!"