from lib.diary import *
from lib.diary_entry import *
from lib.contacts import *
import pytest

"""
Given a single entry 
#adds entry and returns the list of entries
"""

def test_add_new_entry_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry", "Walked the dog")
    diary.add(entry_1) 
    assert diary.all() == [entry_1]

"""
Given multiple entries
#adds them all and returns a list of the entries
"""

def test_add_multiple_new_entry_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish")
    diary.add(entry_1) 
    diary.add(entry_2) 
    assert diary.all() == [entry_1, entry_2]

"""
Given two diary entries are added
#returns an integer of the number of words in the contents 
"""

def test_count_words_in_all_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish")
    diary.add(entry_1) 
    diary.add(entry_2) 
    assert diary.count_words() == 6

"""
Given two diary entries are added
#returns an integer of the amount of time taken to read all diary entries
"""

def test_reading_time_for_2_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish")
    diary.add(entry_1) 
    diary.add(entry_2) 
    assert diary.reading_time(3) == 2

"""
Given zero wpm reading speed
#returns zero
"""

def test_reading_time_for_zero_wpm():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish")
    diary.add(entry_1) 
    diary.add(entry_2) 
    with pytest.raises(Exception) as e:
        diary.reading_time(0)
    error_message = str(e.value)
    assert error_message == "You cannot read anything with 0 wpm"

"""
Given two diary entries are added and a wpm of greater than the number of words
#returns an integer of the amount of time taken to read all diary entries
"""

def test_reading_time_for_2_entries_8_wpm():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish")
    diary.add(entry_1) 
    diary.add(entry_2) 
    assert diary.reading_time(8) == 1

"""
Given two diary entries of differing sizes and a wpm
#returns the entry that has the same words as wpm
"""

def test_best_entry_with_wpm_of_3():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish, and walked the dog all in the same day, it was hard")
    diary.add(entry_1) 
    diary.add(entry_2) 
    assert diary.find_best_entry_for_reading_time(3, 1) == entry_1

"""
Given two diary entries of differing sizes
#returns the entry that is closest to the size the user can read
"""

def test_best_entry_to_read_with_closest_word_count():
    diary = Diary()
    entry_1 = DiaryEntry("Todays entry 1", "Walked the dog")
    entry_2 = DiaryEntry("Todays entry 2", "Take out rubbish, and walked the dog all in the same day, it was hard")
    diary.add(entry_1) 
    diary.add(entry_2) 
    assert diary.find_best_entry_for_reading_time(10, 2) == entry_2

"""
Given a diary entry with a phone number in
#adds phone number to contacts list
"""
def test_number_added_to_contacts_if_in_diary_entry():
    diary = Diary()
    contacts_list = Contacts()
    entry_1 = DiaryEntry("Todays entry 1", "Called doctors on 05647398261")
    diary.add(entry_1)
    diary.check_for_number(contacts_list, entry_1)
    assert contacts_list.all() == ["05647398261"]

"""
Given two diary entries with phone numbers in
#adds phone number to contacts list and returns both
"""
def test_multiple_numbers_added_to_contacts_if_in_diary_entry():
    diary = Diary()
    contacts_list = Contacts()
    entry_1 = DiaryEntry("Todays entry 1", "Called doctors on 05647398261")
    diary.add(entry_1)
    entry_2 = DiaryEntry("Todays entry 1", "Called doctors on 05647398256")
    diary.add(entry_2)
    diary.check_for_number(contacts_list, entry_1)
    diary.check_for_number(contacts_list, entry_2)
    assert contacts_list.all() == ["05647398261", "05647398256"]

"""
Given two diary entries with no phone numbers in
#returns empty contact list
"""
def test_multiple_entries_added_with_no_numbers():
    diary = Diary()
    contacts_list = Contacts()
    entry_1 = DiaryEntry("Todays entry 1", "Called doctors")
    diary.add(entry_1)
    entry_2 = DiaryEntry("Todays entry 1", "Called doctors")
    diary.add(entry_2)
    diary.check_for_number(contacts_list, entry_1)
    diary.check_for_number(contacts_list, entry_2)
    assert contacts_list.all() == []

"""
Given a diary entry with an incorrect phone number length
#returns empty contact list
"""
def test_incorrect_phone_number_not_added_to_contacts_list():
    diary = Diary()
    contacts_list = Contacts()
    entry_1 = DiaryEntry("Todays entry 1", "Called doctors 7263514273")
    diary.add(entry_1)
    diary.check_for_number(contacts_list, entry_1)
    assert contacts_list.all() == []