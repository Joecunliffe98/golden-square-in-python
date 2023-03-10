class TodoList:
    def __init__(self):
        self.list_of_todo = []

    def add(self, todo):
        self.list_of_todo.append(todo)
    
    def incomplete(self):
        incomplete_list = []
        for entry in self.list_of_todo:
            if entry.complete == False:
                incomplete_list.append(entry)
        return incomplete_list

    def complete(self):
        complete_list = []
        for entry in self.list_of_todo:
            if entry.complete == True:
                complete_list.append(entry)
        return complete_list

    def give_up(self):
        for entry in self.list_of_todo:
            entry.mark_complete()