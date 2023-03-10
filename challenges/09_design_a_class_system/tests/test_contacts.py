from lib.contacts import *

"""
Given a number
Adds it to the contacts list
"""
def test_adds_to_contacts():
    contacts_list = Contacts()
    contacts_list.add("05637183923")
    assert contacts_list.all() == ["05637183923"]

"""
Given multiple numbers
Adds them to contacts list
"""
def test_adds_multiple_numbers_to_contacts():
    contacts_list = Contacts()
    contacts_list.add("05637183923")
    contacts_list.add("06372859354")
    assert contacts_list.all() == ["05637183923", "06372859354"]