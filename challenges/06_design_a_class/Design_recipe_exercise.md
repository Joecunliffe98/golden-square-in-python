1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

class Tasks():

    def __init__(self):
        List: To store all of the tasks set
              self.task_list = []

    def add_task(self, task)
        String: Details of the task
        Adds task to self.task_list

    def see_tasks(self):
        Returns self.task_list

    def complete_task(self, task):
        String: The task to be removed
        Removes task from self.task_list


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
Given a task
#adds task to list and shows the list
"""
new_task = Tasks()
new_task.add_task("Walk the dog")
assert new_task.see_tasks() = ["Walk the dog"]

"""
Given no task
#adds raises an exception
"""
new_task = Tasks()
new_task.add_task("") # raises an error with the message "No task set."

"""
Given a task 
#complete_task removes task from list and shows the list
"""
new_task = Tasks()
new_task.add_task("Walk the dog")
new_task.complete_task("Walk the dog")
assert new_task.see_tasks() = []

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.