class Tasks():
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        if task == "":
            raise Exception("No task set.")
        else:
            self.task_list.append(task)
    
    def see_tasks(self):
        return self.task_list
    
    def complete_task(self, task):
        self.task_list.remove(task)