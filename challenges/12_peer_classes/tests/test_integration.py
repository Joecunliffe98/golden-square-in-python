from lib.diary import *
from lib.secret_diary import *
import pytest

"""
Tests that diary is initially locked
"""
def test_secret_diary_is_initially_locked():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    assert secret_diary.locked == True

"""
Tests that diary can be unlocked
"""
def test_secret_diary_can_be_unlocked():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.locked == False

"""
Tests that diary can be read while unlocked
"""
def test_diary_can_be_read_while_unlocked():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My contents"

"""
Tests that Go Away message is shown when diary is locked
"""
def test_go_away_message_shows_when_diary_is_locked():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go Away!"

"""
Tests that diary can be locked once unlocked
"""
def test_diary_can_be_locked_from_unlocked():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My contents"
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go Away!"