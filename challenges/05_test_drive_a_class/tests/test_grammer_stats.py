from lib.grammar_stats import *
import pytest

def test_check_returns_true_if_correct_grammar():
    grammer_check = GrammarStats()
    assert grammer_check.check("Test okay.") == True

def test_check_returns_false_if_no_caps():
    grammer_check = GrammarStats()
    assert grammer_check.check("test not okay.") == False

def test_check_returns_false_if_no_punctuation():
    grammer_check = GrammarStats()
    assert grammer_check.check("Test not okay") == False

def test_percentage_good_returns_correct_percentage():
    grammer_check = GrammarStats()
    grammer_check.check("Test not okay")
    grammer_check.check("test not okay.")
    grammer_check.check("Test okay.")
    assert grammer_check.percentage_good() == 33