def check_to_do(task_list):
    if task_list == None:
        raise Exception("Error: None value passed as argument")
    new_list = []
    if task_list == []:
        new_list = "Input list is empty"
    for items in task_list:
        if "#TODO" in items:
            new_list.append(items)
    if new_list == []:
        new_list = "Nothing in to do list"
    return new_list
