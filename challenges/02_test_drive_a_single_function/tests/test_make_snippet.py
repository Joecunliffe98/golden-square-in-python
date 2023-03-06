from lib.make_snippet import make_snippet

"""
Returns first 5 words of a string
"""

def test_make_snippet_returns_correct_value():
    result = make_snippet("Hello world, my name is Joe!")
    assert result == "Hello world, my name is..."

"""
Returns all of the words in a string if it is less than 5 words
"""

def test_make_snippet_returns_all_words():
    result = make_snippet("Hello world")
    assert result == "Hello world"

"""
Tests if nothing is returned if the string is empty
"""

def test_make_snippet_empty_string():
    result = make_snippet("")
    assert result == ""
