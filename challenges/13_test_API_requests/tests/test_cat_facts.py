from lib.cat_facts import *
from unittest.mock import Mock

def test_provide_cat_fact():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"Cats' eyes shine in the dark because of the tapetum, a reflective layer in the eye, which acts like a mirror.","length":109}
    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: Cats' eyes shine in the dark because of the tapetum, a reflective layer in the eye, which acts like a mirror."