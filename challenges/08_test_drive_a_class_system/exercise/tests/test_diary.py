from lib.diary import *
from lib.diary_entry import *
import pytest

def test_create_new_diary():
    diary = Diary()
    
def test_error_when_diary_is_empty():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.all()
    error_message = str(e.value)
    assert error_message == "Diary is empty"
