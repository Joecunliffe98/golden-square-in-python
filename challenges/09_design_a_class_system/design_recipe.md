1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
┌───────────────────────────┐    ┌───────────────────────┐    ┌───────────────────────┐
│ Contacts()                │    │ Diary()               │    │ ToDoList()            │
│                           │    │                       │    │                       │
│ - grab_contacts_from_diary│    │ - entries             │    │ - tasks               │
│ - add_to_list             ├────┤ - add entry           ├────┤ - add_task            │
│ - retrieve_list           │    │ - read_entries        │    │ - see_tasks           │
│                           │    │ - read_based_on_time  │    │ - see_incomplete_tasks│
└───────────────────────────┘    └───────────┬───────────┘    │ - see_complete_tasks  │
                                             │                │ - give_up_on_all_tasks│
                                             │                └──────────┬────────────┘
                                 ┌───────────┴───────────┐               │
                                 │ DiaryEntry()          │    ┌──────────┴──────────┐
                                 │                       │    │ ToDo()              │
                                 │ - format              │    │                     │
                                 │ - add entry           │    │ - tasks             │
                                 │ - count_words         │    │ - mark_complete     │
                                 │ - reading_time        │    └─────────────────────┘
                                 │ - reading_chunk       │
                                 └───────────────────────┘

Also design the interface of each class in more detail.

class ToDoList:
    def __init__(self):
        Create list

    def add(self, track):
        # Parameters:
        #   Task: an instance of a todo task
        # Side-effects:
        #   Adds the task to the self list

    def incomplete(self):
        # Returns:
        #   A list of the tasks that have not been completed yet
    
    def complete(self):
        # Returns:
        #   A list of the tasks that have been completed
    
    def give_up(self):
        # Sets all tasks in the list to complete


class ToDo:
    def __init__(self, task):
        # Parameters:
        #   task: string
        # Side-effects:
        #   Sets the task and the complete property to false

    def mark_complete(self):
        # Returns:
        #   Sets the complete property to True
        
    
Class DiaryEntry:
    def __init__(self, title, contents):
        # Paramters:
        # title: string
        # contents: string
        # Side_effects:
        # Sets title to self.title and contents to self.contents
    
    def format(self):
       # Returns the title and contents as a formatted string
    
    def count_words(self):
        # Returns the length of the contents if the contents is not empty
    
    def reading_time(self, wpm)
        # Parameters:
        # wpm: as integer
        # Returns the amount of time to read the contents of that entry
    
    def reading_chunk(self, wpm, minutes):
        # Paramters: 
        # wpm: as integer
        # minutes: as integer
        # Returns the biggest passage that the user can read in the given time
    
Class Diary:
    def __init__(self):
        # Returns a list of diary entries 

    def add(self, entry):
        # Parameters:
        # entry: as string
        # Returns nothing
        # Side_effects: Adds the entry to the diary list

    def all(self):
        # Returns diary entries list if it is not empty

    def count_words(self):
        # Returns the word count for all of the entries in the diary list

    def reading_time(self, wpm):
        # Parameters:
        # wpm: as integer
        # Returns the estimated time taken to read all of the entries in the diary

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Paramters:
        # wpm: as integer 
        # minutes: as integer
        # Returns the longest entry that the user can read from the diary list
    
    def check_for_number(self, contacts, entry):
        # Parameters:
        # contacts: as class
        # entry: as string
        # adds phone number to contacts list if one is present
    
Class Contacts:
    def __init__(self):
        Create list

    def add(self, phone_number):
        # Parameters:
        #   phone_number: a string of numbers
        # Side-effects:
        #   Adds the number to the contacts list
    
    def all(self):
        # Returns a list of all the added phone numbers unless the list is empty

    
Class 
    
1. Create Examples as Integration Tests

"""
Given a task
#adds it to the todo list
"""
def test_task_adds_to_todo_list():
    task_1 = Todo("Task 1")
    todo_list = TodoList()
    todo_list.add(task_1)
    assert todo_list.list_of_todo == [task_1]

"""
Given two tasks
#adds them to the todo list
"""
def test_multiple_task_adds_to_todo_list():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.list_of_todo == [task_1, task_2]

"""
Given one complete task and one incomplete task
#returns a list of the incomplete tasks
"""
def test_incomplete_list():
    task_1 = Todo("Task 1")
    task_1.mark_complete()
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_2]

"""
Given one complete task and one incomplete task
#returns a list of the completed tasks
"""
def test_complete_list():
    task_1 = Todo("Task 1")
    task_1.mark_complete()
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.complete() == [task_1]

"""
Given two incomplete tasks
#marks all tasks as complete and returns complete list
"""
def test_give_up():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    assert todo_list.complete() == [task_1, task_2]

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
def test_number_added_to_contacts_if_in_diary_entry
    diary = Diary()
    contacts_list = Contacts()
    entry_1 = DiaryEntry("Todays entry 1", "Called doctors on 05647398261")
    assert contacts_list.all() == "05647398261"

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

4. Create Examples as Unit Tests

"""
Given a task
#adds it as a task and makes sure it is not complete yet
"""
def test_add_task_and_check_not_complete():
    task_1 = Todo("Walk the dog")
    assert task_1.complete == False

"""
Given a task
#adds it as a task and sets it to complete
"""
def test_add_task_and_set_to_complete():
    task_1 = Todo("Walk the dog")
    task_1.mark_complete()
    assert task_1.complete == True

def test_diary_entry_format():
    todays_entry = DiaryEntry("My Title", "These are the contents")
    todays_entry = todays_entry.format()
    assert todays_entry == "My Title: These are the contents"

def test_diary_count_words():
    todays_entry = DiaryEntry("My Title", words_238)
    todays_entry = todays_entry.count_words()
    assert todays_entry == 238
    todays_entry = DiaryEntry("My title", "")
    assert todays_entry.count_words() == "The contents is empty"
    todays_entry = DiaryEntry("My title", words_476)
    assert todays_entry.count_words() == 476

def test_diary_entry_reading_time():
    todays_entry = DiaryEntry("My Title", words_238)
    assert todays_entry.reading_time(238) == 1
    todays_entry = DiaryEntry("My title", "")
    assert todays_entry.reading_time(238) == "The contents is empty"

def test_diary_entry_reading_chunk_238_words():
    todays_entry = DiaryEntry("My Title", words_238)
    assert todays_entry.reading_chunk(238, 1) == "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus"

def test_diary_entry_reading_chunk_476_words():
    todays_entry = DiaryEntry("My Title", words_476)
    assert todays_entry.reading_chunk(238, 2) == "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus"

def test_diary_entry_reading_chunk_called_twice():
    todays_entry = DiaryEntry("My Title", "Lorem ipsum dolor sit amet, consectetuer")
    assert todays_entry.reading_chunk(3, 1) == "Lorem ipsum dolor"
    assert todays_entry.reading_chunk(3, 1) == "sit amet, consectetuer"

def test_diary_entry_reading_chunk_starts_from_beginning():
    todays_entry = DiaryEntry("My Title", "Lorem ipsum dolor sit amet, consectetuer")
    assert todays_entry.reading_chunk(4, 1) == "Lorem ipsum dolor sit"
    assert todays_entry.reading_chunk(4, 1) == "amet, consectetuer"
    assert todays_entry.reading_chunk(4, 1) == "Lorem ipsum dolor sit"

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
def test_adds_to_contacts():
    contacts_list = Contacts()
    contacts_list.add("05637183923")
    contacts_list.add("06372859354")
    assert contacts_list.all() == ["05637183923", "06372859354"]



5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.