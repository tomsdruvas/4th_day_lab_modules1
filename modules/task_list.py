from data.task_list import *
# MVP




def mark_task_complete(task):
    task["completed"] = True

# Extensions

# create a task
def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

# add a task to the list
def add_to_list(list, task):
    list.append(task)

